with open('dataset_3363_2.txt', 'r', encoding='utf8') as file:
    t = ''
    text = file.read()
    print(text)
    for i in range(len(text)):
        if text[i].isdigit() and text[i + 1].isdigit() and text[i - 1].isdigit() == False:
            t += text[i - 1] * int(text[i] + text[i + 1])
        elif text[i].isdigit() and text[i + 1].isdigit() == False and text[i - 1].isdigit() == False:
            t += text[i - 1] * int(text[i])
    print(t)    