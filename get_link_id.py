#link = "https://cdn.bunkr.is/0gxhxgx6b4fr2p11dq9qq_source-Gz1RrIPF.mp4"
def get_link_id(link):
    lst = []
    for i in link:
        lst.append(i)

    lst2 = lst[21:]
    #print(lst2)
    link_id = ""
    for i in lst2:
        link_id += i
    #print(link_id)
    return link_id
    
    
    
        
