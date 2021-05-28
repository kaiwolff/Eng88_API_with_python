#APIs

Stands for Application Programming Interface.

**An API (Application Programming Interface) is a set of functions that allows applications to access data and interact with external software components, operating systems, or microservices. To simplify, an API delivers a user response to a system and sends the system's response back to a user.**

Need to have:


 - network connectivity
 - App used must be accessible at both ends

There are status codes, which are sometimes seen in for example websites (e.g. the infamous 404 error).

API Calls are behind almost any tracking in apps, e.g. live delivery tracking. Almost any automated messages require API calls. Generally speaking, APIs allow us to communicate with websites and applications. An exercise in using API calls was described in the api_task_readme, providing a more hands-on demonstration of API functionality.

Following on from this, I added a function that shows the user the available keys and lets them choose a piece of data they would like to have displayed.

```python

import requests
#need ot import json to read "bytes" class
import json
def get_postcode():
    #prompts user for input of a postcode. runs until valid postcode in correct format is entered
    while True:
        postcode = input("please enter a valid UK postcode, without any spaces:")

        if postcode_exists(postcode) == True:
            return postcode
        else:
            print("Invalid postcode")
            continue

def postcode_exists(postcode):
    #checks if postcode returns status 200 from postcodes.io
    postcode = postcode.lower()
    post_api_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")

    if str(post_api_response.status_code) == "200": #200 is the response that signifies the website is responding.
        #print(f"Postcode {postcode} exists. Status code {post_api_response.status_code}")
        return True
    else:
        #print("The postcode is incorrect, please enter the correct postcode.")
        return False

def get_constituency(postcode):
    #should print the parliamentary constituency.
    api_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")
    constituency = json.loads(api_response.content)["result"]["parliamentary_constituency"]
    print(f"Your constituency is: {constituency}")

def collect_info(postcode):
    #quick function to collect available info into a dictionary:
    api_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")
    #json loads converts the json into a python dictionary that I can actually work with
    return json.loads(api_response.content)["result"]

def show_info(postcode):
    available_info = collect_info(postcode)
    print("here is the available information")
    for key in available_info.keys():
        print(key)

    desired_info = input("which bit of info would you like to know? ")
    if desired_info in available_info.keys():
        print(available_info[desired_info])

postcode = get_postcode()
# get_constituency(postcode)
# show_info(postcode)
```