import requests

r = requests.get("https://subtitles-for-youtube.p.rapidapi.com/subtitles/VrMHA3yX_QI?translated=None&type=None",
                 headers={"X-RapidAPI-Host": "subtitles-for-youtube.p.rapidapi.com",
                          "X-RapidAPI-Key": "042f3fd40bmsh299a3d264e6259ep190110jsnf075030f8fec"})

print(type(r.json()))
print(r.json())

"""
{
    'index': 151, 
    'start': 513.82, 
    'dur': 2.627, 
    'end': 516.447, 
    'text': 'The system actually\nlooked like that.'
    }
"""