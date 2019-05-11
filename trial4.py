import requests

r = requests.get("https://subtitles-for-youtube.p.rapidapi.com/subtitles/VrMHA3yX_QI?translated=None&type=None",
                 headers={"X-RapidAPI-Host": "subtitles-for-youtube.p.rapidapi.com",
                          "X-RapidAPI-Key": "042f3fd40bmsh299a3d264e6259ep190110jsnf075030f8fec"})

print(r.json())
