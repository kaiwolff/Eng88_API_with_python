#Use python to make an API call using a package called requests
#dependency is pip (package manager). Use pip to install requests using 'pip install requests'
#The above is required for every new project, as it needs to be installed in every new virtual environment
import requests
#need ot import json to read "bytes" class
import json

#firstly, let's test out the response if we get one from the bbc website
response_bbc = requests.get("https://www.bbc.co.uk/")
#print out to see. if 200, this means the website works as intended.
# print(response_bbc)
# print(response_bbc.status_code)
# print(response_bbc.headers) # This line will bring otu all the ehaders we are able to get. Quite a lot of data.
# print(response_bbc.headers)
# data_headers = response_bbc.headers
#
# for date_in in data_headers.keys():
#     print(date_in)
#
#
# # print(type(response_bbc.headers))
# postcode = "S101GG"

def postcode_exists(postcode):

    postcode = postcode.lower()
    post_api_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")

    if str(post_api_response.status_code) == "200": #200 is the response that signifies the website is responding.
        print(f"Postcode {postcode} exists. Status code {post_api_response.status_code}")

    else:
        print("The postcode is incorrect, please enter the correct postcode.")


postcode_exists("s101gg")itemsname