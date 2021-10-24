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

from leanlauncher_keys import LEANLAUNCHER_CLIENT, LEANLAUNCHER_SECRET, LEANLAUNCHER_REDIRECT_URI

import webbrowser

## functions ##
def leanlauncher_open_auth_microsoft():
  """
  Attempts to open the authentication URL in the browser using the webbrowser
  module. If the browser cannot be opened, a link will be provided for the user
  to manually open instead.

  Returns:
    A Dictionary containing launcher information on successful authentication,
    None otherwise
  """

  url = minecraft_launcher_lib.microsoft_account.get_login_url(LEANLAUNCHER_CLIENT, LEANLAUNCHER_REDIRECT_URI)
  code = ""

  print("Please open the following URL in your web browser and complete the authentication:")
  print(f"{url}")

  print("Attempting to open link for you...")

  try:
    webbrowser.open(url, 2, True)
  except webbrowser.Error:
    print("Could not open the web browser automatically; you will need to enter the URL manually.")

  print("Once logged in, enter the URL you are redirected to here:")
  code_url = input("> ")

  if not minecraft_launcher_lib.microsoft_account.url_contains_auth_code(code_url):
    print("Not a valid URL! Returning to main menu...")
    return None
  else:
    code = minecraft_launcher_lib.microsoft_account.get_auth_code_from_url(code_url)

  print(f"CODE: {code}")

  options = minecraft_launcher_lib.microsoft_account.complete_login(LEANLAUNCHER_CLIENT, LEANLAUNCHER_SECRET, LEANLAUNCHER_REDIRECT_URI, code)

  return options
