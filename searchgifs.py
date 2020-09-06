import urllib.request
from keys import YOUR_API_KEY
import json
import os
import sys



if __name__ == "__main__":
    search_term = sys.argv[1]
    limit = sys.argv[2]

    search_term = search_term.replace(" ", "+")
    
    if not os.path.isdir(search_term):
        os.mkdir(search_term)

    print(search_term)

    data=json.loads(urllib.request.urlopen(f"http://api.giphy.com/v1/gifs/search?q={search_term}&api_key={YOUR_API_KEY}&limit={limit}").read())
    gif_ids = [d["id"] for d in data["data"]]

    for i, id in enumerate(gif_ids):
        url = f"https://media.giphy.com/media/{id}/giphy.gif"
        print(url,i)
        os.system(f"curl {url} --output {search_term}/{search_term}{i}.gif")
        
