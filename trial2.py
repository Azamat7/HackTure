# -*- coding: utf-8 -*-

# Sample Python code for youtube.captions.download
# NOTE: This sample code downloads a file and can't be executed via this
#       interface. To test this sample, you must run it locally using your
#       own API credentials.

# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import io
import os

import googleapiclient.discovery

from googleapiclient.http import MediaIoBaseDownload


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCDsSS0qWdJrx9Xmdbuk5FWP-ROzpzRGCw"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.captions().download(
        id="1pp4kcouz0ZWMm5VxLPveU0mqCS36FtaSLQTRm5IMRQ="   
    )
    # TODO: For this request to work, you must replace "YOUR_FILE"
    #       with the location where the downloaded content should be written.
    fh = io.FileIO("/home/azret/PycharmProjects/tryAza/caption", "wb")

    download = MediaIoBaseDownload(fh, request)
    complete = False
    while not complete:
        status, complete = download.next_chunk()


if __name__ == "__main__":
    main()
