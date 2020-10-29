

def error_form_list(errors):
    errors=errors.replace("</ul>","")
    errors=errors.replace("</li>","")
    errors=errors.replace("__all__"," ")
    list_errors=[x.split("<li>") for x in errors.split("<ul")]
    for item in list_errors:
        n=len(item)
        i=0
        while(i<n):
            item.pop(i)
            n-=1
            i+=1
    vacio=[]
    espacio=[" "]
    if list_errors.count(vacio)>0:
        list_errors.remove(vacio)
    if list_errors.count(espacio)>0:
        list_errors.remove(espacio)
    return list_errors