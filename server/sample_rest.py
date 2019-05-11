import json
import os

from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import googleapiclient.discovery
import requests


app = Flask(__name__)
CORS(app)

api = Api(app)


@app.route("/videos", methods=["POST"])
def get_video_list():
    data = request.get_json()
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCDsSS0qWdJrx9Xmdbuk5FWP-ROzpzRGCw"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    query = youtube.search().list(
        part="snippet",
        q=data["query"],
        maxResults=15
    )

    response = query.execute()
    return json.dumps(response)


@app.route("/subtitles", methods=["POST"])
def get_video_subtitles():
    data = request.get_json()

    r = requests.get(
        "https://subtitles-for-youtube.p.rapidapi.com/subtitles/"
        f"{data['videoID']}?translated=None&type=None",
        headers={
            "X-RapidAPI-Host": "subtitles-for-youtube.p.rapidapi.com",
            "X-RapidAPI-Key":
                "042f3fd40bmsh299a3d264e6259ep190110jsnf075030f8fec"})
    return json.dumps(r.json())


@app.route("/wiki", methods=["POST"])
def get_wiki():
    data = request.get_json()
    keyword = data["keyword"]

    print(data)
    print(keyword)

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--lang=en")
    driver = webdriver.Chrome(chrome_options=options)

    driver.get("https://www.google.com/")
    english = driver.find_element_by_xpath('//a[contains(text(), "English")]')
    english.send_keys(Keys.ENTER)

    q = driver.find_element_by_name("q")
    q.send_keys(keyword, Keys.ENTER)

    knowledge_panel = driver.find_element_by_xpath(
        '//div[contains(@class, "knowledge-panel")]')

    code = knowledge_panel.get_attribute("innerHTML")
    print(code)

    return code


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
