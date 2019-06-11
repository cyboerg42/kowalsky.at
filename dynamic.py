# Peter Kowalsky - 10.06.19

def html_head(title):
    head = "<html><head>"
    # Skeleton CSS
    head = head + '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.css">'
    # Menu
    head = head + '<style>' + open("css/menu.css", "r").read() + '</style>'
    head = head + '<script>' + open("js/menu.js", "r").read() + '</script>'
    # Title
    head = head + "<title>" + title + "</title>"
    head = head + "</head>"
    return head

def top_bar(active):
    html = '<div class="navBar" id="mainNavBar">\n'
    html = html + '<a href="/">Home</a>\n'
    html = html + '<a href="/blog">Blog</a>\n'
    html = html + '<a href="/services">Services</a>\n'
    html = html + '<a href="/about">About Us</a>\n'
    html = html + '<a href="/contact">Contact</a>\n'
    html = html + '<a href="javascript:void(0);" class="icon" onClick="openDrawerMenu()">&#9776;</a>\n'
    html = html + '</div><br>'
    return html
