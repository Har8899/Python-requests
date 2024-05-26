import requests
file = requests.get('https://quotes.toscrape.com/')
html2 = file.text
with open('Authors.txt', 'w') as f:
    for author in html2.split('\n'):
        if '<span>by <small class="author" itemprop="author">' in author:
            author = author.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
            author = author.strip()
            f.write(author)
            f.write('\n')