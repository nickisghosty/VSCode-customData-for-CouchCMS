from urllib.request import urlopen
from bs4 import BeautifulSoup
from markdownify import markdownify


html=urlopen("https://docs.couchcms.com/tags-reference.html")
bsObj = BeautifulSoup(html, "lxml")
art = bsObj.find("article")
f=open("html.html-data.json", "w+")
f.write("{" + "\n" + "    \"version\":1.1," + "\n" + "    \"tags\":[" + "\n")
for tag in art.find_all("li"):
    taglink = "http://docs.couchcms.com/" + tag.a["href"]
    taghtml = urlopen(taglink)
    tagbs = BeautifulSoup(taghtml,"lxml")
    tagart = tagbs.find("article")
    tagname = tagart.h1.get_text()
    mdart = markdownify(tagart.encode("utf-8"))
    md = [line for line in mdart.split("\n")]
    mdd = '\\n'.join(mdart.split("\n"))
    listt = []
    listtt = ""
    par = tagart.h2.find_next("ul")
    try:
        for line in par.find_all("li"):
            if not line.a:
                listt.extend(line)
        
    except BaseException:
        pass
    f.write("        {" + " \n" + "            \"name\":\"cms:" + tagname + "\"," + "\n" + "            \"description\":\"" + mdd + "\"," + "\n"+"            \"attributes\":[" + "\n")
    if not listt == []:
       # print(listt)
        for ea in listt:
            listttt = []
            output=""
            try:
                next_tag = tagart.find("h3", id=(ea))
                tagBreak = next_tag.name
                if next_tag:
                    for tag in next_tag.next_siblings:
                        if tag.name == tagBreak:
                            break
                        else:
                             if str(tag).strip() != "":
                                output += str(tag)

                    next_tag = next_tag.next_sibling
                
                    k = markdownify(output)
                    kkk=[line for line in k]
                    n = "".join(kkk)
                    g = "\\n".join(n.split("\n"))
                    h="\\n".join(g.split("\n"))
                    
                    listttt.append(h)
                    x = listttt
                    jk = x[0:len(x)] = [''.join(x[0:len(x)])]
                    desc = jk[0]
                                            
                    f.write("{"+"\n"+"\"name\": \"" + ea + "\"," + "\n" + "\"description\":\"" + desc + "\"," + "\n" + "\"values\":[" + "\n" + "{" + "\n" + "\"name\":\"\"" + "\n"+ "}"+ "\n" + "]" + "\n"+ "},")
                            
            except BaseException:
                pass
    f.write("\n"+"]"+"\n"+"},")      
    
f.write("}"+"\n"+"]"+"\n"+"}")