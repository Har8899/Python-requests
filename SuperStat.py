import requests
import json


with open('SuperStat.txt', 'a', encoding='utf-8') as f:
    for i in range(1,4):
        url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?genre=706;;page={i}'
        res = requests.get(url)
        data = json.loads(res.text)

        for headline in data:
            f.write(headline['headline'])
            f.write('\n')