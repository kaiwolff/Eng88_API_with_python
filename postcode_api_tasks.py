import requests
#need ot import json to read "bytes" class
import json

def postcode_exists(postcode):

    postcode = postcode.lower()
    post_api_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")

    if str(post_api_response.status_code) == "200": #200 is the response that signifies the website is responding.
        print(f"Postcode {postcode} exists. Status code {post_api_response.status_code}")

    else:
        print("The postcode is incorrect, please enter the correct postcode.")


postcode_exists("s101gg")