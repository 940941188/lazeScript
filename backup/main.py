#!/usr/bin/python
import os
from plumbum import colors, cli
from plumbum.cmd import cp, mv

abs_path = os.path.abspath('.')

vs_code_config_path=os.path.expanduser("~/.config/Code - OSS/User")
vs_code_backup_path = os.path.join(abs_path, 'vs_code')
vs_code_files = ['keybindings.json', 'settings.json', 'snippets']


class BackupApp(cli.Application):
  VERSION=colors.blue | "1.0.0"

  def init_backup_vscode(self):
    if not os.path.exists(vs_code_backup_path):
      os.mkdir(vs_code_backup_path)
      print(colors.green | ("created %s" % vs_code_backup_path))

  def backup_vscode(self):
    for file_name in vs_code_files:
      target_path = os.path.join(vs_code_config_path, file_name)
      if os.path.exists(target_path):
        cp("-r", target_path, vs_code_backup_path)
        print(colors.green | ('cp %s' % target_path))
      else:
        print(colors.red | ('file not found: %s' % target_path))
    print("vscode config backup completed")

  def recover_vscode(self):
    for file_name in vs_code_files:
      target_path = os.path.join(vs_code_config_path, file_name)
      backup_file_path = os.path.join(vs_code_backup_path, file_name)
      if os.path.exists(backup_file_path):
        if os.path.isdir(target_path):
          cp("-rf", backup_file_path, vs_code_config_path)
        else:
          cp("-f", backup_file_path, target_path)
        print(colors.green | ('cp %s covers %s' % (backup_file_path, target_path)))
      else:
        print(colors.red | ('file not found: %s' % target_path))
    print("vscode config recover completed")

  @cli.switch(["-b", "--backup"], help="backup config")
  def backup(self):
    print("start backup")
    # backup vscode config
    self.init_backup_vscode()
    self.backup_vscode()
    print("backup completed")

  @cli.switch(["-r", "--recover"], cli.Set("all", "vscode"), help="recover config")
  def recover(self, mode):
    if mode == 'vscode':
      self.recover_vscode()

  def main(self):
    pass


if __name__ == "__main__":
  BackupApp.run()
