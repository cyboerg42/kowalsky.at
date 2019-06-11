# Peter Kowalsky - 10.06.19

import os
from datetime import datetime
from utils import list_all_files_in_dir

empty_string = ''

def dynamic(txt_src_folder):
  files = list_all_files_in_dir(txt_src_folder, ".md")
  md = ""
  i = 1
  for f in files:
    last_modified = datetime.utcfromtimestamp(int(os.stat(txt_src_folder + f).st_mtime)).strftime('%Y-%m-%d %H:%M:%S')
    f = f.replace(".md", empty_string)
    md = md + "\n" + str(i) + ". " + "[" + f + "](/blog/" + f + ") - last modified [" + str(last_modified) + "]"
    i = i + 1
  return md
