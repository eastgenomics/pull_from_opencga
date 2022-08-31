# Import ClientConfiguration and OpencgaClient class
import requests
from config import USER, PASSWORD

# Retrieve keys from JSON 
CLIENT_KEY = USER
USER_KEY = PASSWORD

headers = {
	"Content-Type" :"application/vnd.api+json",
    "X-Auth-Token-Client": CLIENT_KEY,
    "X-Auth-Token-Account": USER_KEY
}


api_url = 'https://uat.eglh.app.zettagenomics.com/opencga/'

response = requests.request("GET", api_url, headers=headers)

print(response)
