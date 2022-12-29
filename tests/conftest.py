import logging
import pytest

from datetime import datetime
from py.xml import html


@pytest.fixture(scope="session")
def log():
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    return log


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("Description"))
    cells.insert(1, html.th("Time", class_="sortable time", col="time"))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    setattr(report, "duration_formatter", "%H:%M:%S.%f")
