#!/bin/sh

# Run all tests and generate reports for both pytest-html and report portal
cd ..
pytest ./tests --html=report.html --self-contained-html -v -m blockchain