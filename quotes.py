import requests

for i in range(1, 11):
    print('Page No. :', i)
    url =f'https://quotes.toscrape.com/page/{i}/'
    res = requests.get(url)
    html = res.text
    with open('quotes.csv', 'a', encoding='utf-8') as f:
        for line in html.split('\n'):

            if '<span class="text" itemprop="text">' in line:
                line = line.replace('<span class="text" itemprop="text">', '').replace('</span>', ' ')
                quote = line.strip()


            if '<span>by <small class="author" itemprop="author">' in line:
                line = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '')
                author = line.strip()

                f.write(author+','+quote)
                f.write('\n')


