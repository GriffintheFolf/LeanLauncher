#!/usr/bin/env python3

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

DEFAULT_INSTALL_PATH = minecraft_launcher_lib.utils.get_minecraft_directory()
LATEST_VERSION = minecraft_launcher_lib.utils.get_latest_version()["release"]

### functions ###

def leanlauncher_download_version(version=LATEST_VERSION, path=DEFAULT_INSTALL_PATH):
  """
  Installs the specified version of Minecraft to the specified path

  Parameters:
    version (str): the version of Minecraft to be installed, by default the latest
    path (str): the path to install Minecraft to, by default ~/.LeanLauncher/versions

  Returns:
    True on successful install, False on error
  """

  try:
    minecraft_launcher_lib.install.install_minecraft_version(version, path)
  except minecraft_launcher_lib.exceptions.VersionNotFound:
    print(f"Not a valid version {version}, please try again")
    return False

  print(f"Minecraft version {version} successfully installed to {path}!")
  return True