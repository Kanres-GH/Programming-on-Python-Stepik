with open('dataset_3363_4.txt', 'r', encoding='utf8') as file:
    text = file.read().splitlines()
    l = []
    for i in text:
        l.append(i.split(';'))
    for i in l:
        i[1] = int(i[1])
        i[2] = int(i[2])
        i[3] = int(i[3])
    for i in l:
        del i[0]
        print(sum(i) / 3)
    s1 = s2 = s3 = cnt = 0
    for i in l:
        s1 += i[0]
        s2 += i[1]
        s3 += i[2]
        cnt += 1
    print(s1 / cnt, s2 / cnt, s3 / cnt, sep = ' ')