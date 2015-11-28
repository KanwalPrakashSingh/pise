import requests
import json


def main():

    # These code snippets use an open-source library.
    response = requests.post("https://camfind.p.mashape.com/image_requests",
      headers={
        "X-Mashape-Key": "Pvn83ortNymshLECCK00pLIOY3BRp1iqBrajsnlMYgVjcidX7n",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      },
      data={
        "focus[x]": "480",
        "focus[y]": "640",
        "image_request[altitude]": "27.912109375",
        "image_request[language]": "en",
        "image_request[latitude]": "35.8714220766008",
        "image_request[locale]": "en_US",
        "image_request[longitude]": "14.3583203002251",
        "image_request[remote_image_url]": "http://upload.wikimedia.org/wikipedia/en/2/2d/Mashape_logo.png"
      }
    )

    print response.text,response.status_code

main()