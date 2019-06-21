## kowalsky.at - Webpage of Peter Kowalsky e.U.
## Peter Kowalsky - 10.06.19

from flask import Flask

from md2html import md2html
from md2html import md_file2html

from utils import check_if_file_exists
from utils import list_all_files_in_dir

from blog import dynamic as blog_dynamic
from dynamic import html_head, top_bar

txt_src_folder = "./txt/"
blog_src_folder = "./txt/blog/"
empty_string = ''

app = Flask(__name__)

@app.route("/")
def main():
    file = open(txt_src_folder + "index.md", "r")
    html = html_head("kowalsky.at") + "<body>" + top_bar('index') + md_file2html(file) # static content
    return html + "</body></html>"

@app.route("/blog")
def blog():
    file = open(txt_src_folder + "blog.md", "r")
    html = html_head("bl0g") + "<body>" + top_bar('blog') + md_file2html(file)
    html = html + md2html(blog_dynamic(blog_src_folder)) # dynamic content
    return html + "</body></html>"

@app.route("/blog/<url>")
def blog_page(url):
    if check_if_file_exists(blog_src_folder + url + ".md"):
      file = open(blog_src_folder + url + ".md", "r")
      return html_head(url.replace(".md", empty_string)) + "<body>" + top_bar('blog') + md_file2html(file) + "</body></html>"
    else:
      return "<h1>404 Not Found</h1>", 404

@app.route("/<url>")
def site(url):
    if check_if_file_exists(txt_src_folder + url + ".md"):
      file = open(txt_src_folder + url + ".md", "r")
      return html_head(url.replace(".md", empty_string)) + "<body>" + top_bar('blog') + md_file2html(file) + "</body></html>"
    else:
      return "<h1>404 Not Found</h1>", 404
