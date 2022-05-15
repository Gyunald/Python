def myxml(tagname, content="", **a):
    atts = "".join([f" {key}='{value}'" for key,value in a.items()])
    return f"<{tagname}{atts}>{content}</{tagname}>"

print(myxml("foo","bar",a=1,b=2,c=3))
