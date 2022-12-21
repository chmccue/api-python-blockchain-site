from main.utils.request import ApiCall

QUERY_URL = 'https://blockchain.info/q/'
REST_URL = 'https://api.blockchain.com/v3/exchange/'

query_request = ApiCall(QUERY_URL)
rest_request = ApiCall(REST_URL)
