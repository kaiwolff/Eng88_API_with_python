import requests
#need ot import json to read "bytes" class
import json
def get_postcode():
    while True:
        postcode = input("please enter a valid UK postcode, without any spaces:")

        if postcode_exists(postcode) == True:
            return postcode
        else:
            print("Invalid postcode")
            continue

def postcode_exists(postcode):

    postcode = postcode.lower()
    post_api_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")

    if str(post_api_response.status_code) == "200": #200 is the response that signifies the website is responding.
        print(f"Postcode {postcode} exists. Status code {post_api_response.status_code}")
        return True
    else:
        print("The postcode is incorrect, please enter the correct postcode.")
        return False

def get_constituency(postcode):
    #should print the parliamentary constituency.
    api_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")
    constituency = json.loads(api_response.content)["result"]["parliamentary_constituency"]
    print(f"Your constituency is: {constituency}")

postcode = get_postcode()
get_constituency(postcode)
