import urllib.request
from keys import YOUR_API_KEY
import json
import os
import sys



if __name__ == "__main__":
    to_translate = sys.argv[1]
    results = int(sys.argv[2])

    # to_translate = to_translate.replace(" ", "+")
    path = f"output/translate/{to_translate}"
    
    if not os.path.isdir(path):
        os.mkdir(path)

    print(to_translate)

    req = f"https://api.giphy.com/v1/gifs/translate?api_key={YOUR_API_KEY}&s={to_translate}"

    gif_ids = []

    data=json.loads(urllib.request.urlopen(req).read())
    gif_id = data['data']['url']

    counter = 0

    while len(gif_ids) < results and counter <= 10:
        if gif_id not in gif_ids:
            gif_ids.append(gif_id)
        else:
            data=json.loads(urllib.request.urlopen(req).read())
            gif_id = data['data']['id']
            counter +=1

    for i, id in enumerate(gif_ids):
        url = f"https://media.giphy.com/media/{id}/giphy.gif"
        print(url,i)
        os.system(f"curl {url} --output {path}/{to_translate}{i}.gif")
        
