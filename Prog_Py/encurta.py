import urllib.parse as up

link =  up.urlparse('https://prairie-heath-fb8.notion.site/Python-60-Horas-387bab83a05543b39e1c36f5e906babb',)

print(link.scheme, link.netloc)