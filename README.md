# Blockchain.com API Python Examples

* Files in main/exchangerestapi implement some Exchange REST API calls from https://api.blockchain.com/v3/
* Files in main/queries implement some query API calls from https://www.blockchain.com/explorer/api/q

### Getting Started

* This repository utilizes [Pipenv](https://pypi.org/project/pipenv/) to build a local environment that does not 
interfere with your systems environment. All dependencies are included in the Pipfile.
1. To install Pipenv, run `pip install pipenv`
2. Load the Pipfile contained in this repository to install the dependencies. 
Follow instructions in Pipenv link above, if neceessary.

### Test Plan

Below is an example test plan for validating queries and REST API data.

#### Query Validation

Note per documentation from site, we should not run extensive query tests:
`Please limit your queries to a maximum of 1 every 10 seconds.`

1. Satoshi's genesis address received more than 60 BTC.
2. 24 hour total BTC sent is greater than 0.

#### Rest API Schema Validation

1. Validate symbol Api calls return correct schema validation (singular and all).
2. Validate ticker Api calls return correct schema validation (singular and all).

#### Rest API Validation

1. TBD


