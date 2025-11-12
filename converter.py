import os

files = os.listdir("markdown")

for file in files:
    f = open("markdown/" + file, "r")
    contents = f.read()
    f.close()
    
    title = contents.split("\n")[0]
    
    f = open("html/" + title + ".html", "w")
    f.write(contents)
    f.close()
