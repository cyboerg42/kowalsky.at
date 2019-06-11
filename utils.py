# Peter Kowalsky - 10.06.19

import os

def check_if_file_exists(path):
  exists = os.path.isfile(path)
  if exists:
    return 1
  else:
    return 0

def list_all_files_in_dir(path, type):
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
    for file in f:
      if type in file:
        files.append(file)
  return files
