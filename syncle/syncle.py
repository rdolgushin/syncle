#!/usr/bin/env python

import sys, os, shutil, time, yaml

src_paths = []
targets_dir = ""
delay = 3

def get_settings():
  global src_paths, targets_dir, delay
  config = yaml.load(open(os.path.expanduser("~/.synclerc.yml")))
  src_paths = config['files']
  targets_dir = config['storage']
  if config['delay']:
    delay = config['delay']

def main():
  global src_paths, targets_dir, delay
  while True:
    get_settings()
    for src_path in src_paths:
      src_path = os.path.expanduser(src_path)
      targets_dir = os.path.expanduser(targets_dir)

      target_path = os.path.join(targets_dir, os.path.split(src_path)[-1])

      src_mtime = os.stat(src_path).st_mtime
      target_mtime = 0
      if os.path.exists(target_path):
        target_mtime = os.stat(target_path).st_mtime

      if src_mtime > target_mtime:
        shutil.copy2(src_path, target_path)
      elif src_mtime < target_mtime:
        shutil.copy2(target_path, src_path)

    time.sleep(delay)
