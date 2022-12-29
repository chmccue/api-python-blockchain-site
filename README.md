# Blockchain.com API Python Examples

* Files in `main/exchangerestapi` implement some Exchange REST API calls from https://api.blockchain.com/v3/
* Files in `main/queries` implement some query API calls from https://www.blockchain.com/explorer/api/q

### Getting Started

* This repository utilizes [Pipenv](https://pypi.org/project/pipenv/) to build an environment that does not 
interfere with a system environment. All dependencies are included in the Pipfile.
1. To install Pipenv, run `pip install pipenv`
2. Load the Pipfile contained in this repository to install the dependencies. 
Follow instructions in Pipenv link above, if necessary.

### Run Tests

1. Run the following file based on your Operating System:
   - For Mac or Linux, execute `runners/run-all-tests-mac-linux.sh`
   - For Windows, execute `runners/run-all-tests-windows.bat`
2. After tests complete, report generates in root of project directory with pass/fail/skip statistics.

### Test Plan

Below is an example test plan for validating queries and REST API data.

#### Query Validation

Note: to respect the Blockchain site documentation, we should not run extensive query tests:
`Please limit your queries to a maximum of 1 every 10 seconds.`

1. Satoshi's genesis address received more than 60 BTC.
2. 24 hour total BTC sent is greater than 0.

#### Rest API Schema Validation

1. Validate symbol Api calls return correct schema validation (singular and multiple).
2. Validate ticker Api calls return correct schema validation (singular and multiple).

#### Rest API Validation

1. TBD

### Pytest Details

#### Markers

- Markers are configured to allow running of specific tests.
- Custom markers are defined in pytest.ini file.
- Skipped tests are marked with skip, along with the reason for being skipped.

#### Report

- Report generated using pytest-html.
- The command to generate the report is in the bash script located in the `runners` directory.
- If you want to generate the report without using the bash script, you need to add it to the run command:
  - `pytest ./tests --html=report.html --self-contained-html`
- Note in the current configuration, generating a new report will overwrite the previous report.
