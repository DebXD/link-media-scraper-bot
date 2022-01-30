
import linkGrabber, re, sys

user_link = input("Enter Your Link : ")
links = linkGrabber.Links(user_link)
grabbed_links = links.find(href=re.compile(".jpg|.mp4"))
sys.stdout = open("mylinks.txt", "w")

for i in range(len(grabbed_links)):
    dic = grabbed_links[i]
    for key, values in dic.items():
        if key  == "href":
            url  =  values
            print(url)

sys.stdout.close()





