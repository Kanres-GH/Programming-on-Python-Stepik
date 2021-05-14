with open('dataset_3380_5.txt', 'r', encoding='utf8') as file:
    classes = dict()
    class_count = dict()
    text = file.read().splitlines()
    l = []
    for i in text:
        l.append(i.split('\t'))
    print(l)
    print()
    s = 0
    for i in l:
        classes[i[0]] = 0
        class_count[i[0]] = 0
    for i in l:
        classes[i[0]] += int(i[2])
        class_count[i[0]] += 1
    print(classes)
    print(class_count)
    for i in range(1, 12):
        t = f'{i} '
        if class_count[str(i)] == 0:
            t += "-"
        else:
            t += str( float( classes[str(i)] / class_count[str(i)] ) )
        print(t)