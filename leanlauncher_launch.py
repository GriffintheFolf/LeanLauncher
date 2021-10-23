"""
LeanLauncher v0.1
Based on minecraft-launcher-lib:
<https://pypi.org/project/minecraft-launcher-lib>

Copyright (c) 2021 Thomas Sirack

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import minecraft_launcher_lib
import subprocess

import leanlauncher_download

### functions ###
def leanlauncher_launch_offline(version):
  """
  Launches the specified version of the game in offline mode,
  that is, without online authentication.

  Parameters:
    version (str): the version of the game to launch
  """

  options = minecraft_launcher_lib.utils.generate_test_options()
  command = minecraft_launcher_lib.command.get_minecraft_command(version, leanlauncher_download.DEFAULT_INSTALL_PATH, options)

  subprocess.call(command)

def leanlauncher_launch_prompt(offline):
  """
  Displays a prompt to launch the game.

  Parameters:
    offline (bool): True if launching in offline mode, False otherwise
  """

  print("""
Launch Minecraft
---------------------
  """)

  version = input("Which version do you want to launch? ")
  if minecraft_launcher_lib.utils.is_version_valid(version, leanlauncher_download.DEFAULT_INSTALL_PATH):
    if offline:
      leanlauncher_launch_offline(version)
    else:
      # TODO: online launching
      pass
  else:
    print(f"Version {version} not found; did you remember to install it?")