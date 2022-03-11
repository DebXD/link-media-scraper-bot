
import linkGrabber, re, time
def remove_dup(lst):
    set1 = set()
    final_list = []
    for i in lst:
        set1.add(i)
    for i in set1:    
        final_list.append(i)
    return final_list
        
    
    
def get_urls(link):
    user_link = link
    links = linkGrabber.Links(user_link)
    grabbed_links = links.find(href=re.compile(".jpg|.mp4"))
    url_list = []
    for i in range(len(grabbed_links)):
        dic = grabbed_links[i]
         
        for key, values in dic.items():
            if key  == "href":
                url  =  values
                url_list.append(url)
                final_list = remove_dup(url_list)
    return final_list








