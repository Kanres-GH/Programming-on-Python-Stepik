import requests
link = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('dataset_3378_3.txt') as inf:
    t = inf.readline().strip()
t = str(requests.get(t).text)
while 'We' not in t:
    print(t)
    t = requests.get(link + t).text
print(t)