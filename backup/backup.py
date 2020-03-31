#!/usr/bin/python
import os
from plumbum import colors
from plumbum.cmd import cp, ls

abs_path = os.path.abspath('.')

vs_code_config_path=os.path.expanduser("~/.config/Code/User")
vs_code_backup_path = os.path.join(abs_path, 'vs_code')
vs_code_files = ['keybindings.json', 'settings.json', 'snippets']

if not os.path.exists(vs_code_backup_path):
  os.mkdir(vs_code_backup_path)

for file_name in vs_code_files:
  target_path = os.path.join(vs_code_config_path, file_name)
  if os.path.exists(target_path):
    print "%s" % target_path
    cp("-r", target_path, vs_code_backup_path)

# print "%s" % ls()
# print "%s" % vs_code_config_path
# print "%s" % vs_code_backup_path

