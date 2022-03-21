def get_url_extension(link):
    lst = []
    for i in link:
        lst.append(i)
    lst2 = lst[-4:]
    extension = ""
    for i in lst2:
        extension += i
    return extension
