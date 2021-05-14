with open('dataset_3363_3.txt','r',encoding='utf8') as file:
    d = dict()
    text = file.read()
    l = text.split()
    print(text)
    for i in l:
        d[i] = 0
    for i in l:
        d[i] += 1
    print(max(d, key = d.get), max(d.values()))