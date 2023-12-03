from django.shortcuts import render
import markdown2
from . import util

def convert_md_to_html(title):
    md_content = util.get_entry(title)
    if md_content == None:
        return None
    else:
        return markdown2.markdown(md_content)

def index(request):
    content = util.list_entries()
    css = util.get_entry("CSS")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content is None:
        return render(request, "encyclopedia/404.html",{"title": title})
    else:
        return render(request, "encyclopedia/entry.html", {"title":title, "content":html_content})
   

