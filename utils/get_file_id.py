def get_file_id(link):
    lst = []
    for i in link:
        lst.append(i)

    lst2 = lst[25:]

    file_id = ""
    for i in lst2:
        if i == "/":
            break;
        else:
            file_id += i
    #print(file_id)
    return file_id     
