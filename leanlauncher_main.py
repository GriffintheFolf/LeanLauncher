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

import leanlauncher_auth_microsoft
import leanlauncher_download
import leanlauncher_launch

### globals ###
LEANLAUNCHER_LAUNCH_OPTIONS = {}

### functions ###

# user input #
def leanlauncher_main_menu():
  """
  Display a list of selections for the user to choose on the main menu,
  and allows the user to choose which one they want.

  Returns:
    Int corresponding to the action desired.
  """

  print("""
Choose one of the following:

1. Launch Minecraft (-WIP-)
2. Launch Minecraft Offline
3. Download Minecraft
4. Authenticate (Mojang) (-WIP-)
5. Authenticate (Microsoft) (-WIP-)
6. LeanLauncher Settings (-WIP-)
7. Quit
  """)

  choice = input("> ")
  if choice.isnumeric():
    choice = int(choice)
    return choice
  else:
    print(f"Invalid selection {choice}, please try again")
    return leanlauncher_main_menu()


# processing #
def leanlauncher_act_upon_choice(choice):
  """
  Performs the action specified by choice.

  Parameters:
    choice (int): the number of the action desired
  """

  if choice == 1:
    leanlauncher_launch.leanlauncher_launch_prompt(False, LEANLAUNCHER_LAUNCH_OPTIONS)
  elif choice == 2:
    leanlauncher_launch.leanlauncher_launch_prompt(True, None)
  elif choice == 3:
    leanlauncher_download.leanlauncher_download_prompt()
  elif choice == 4:
    pass
  elif choice == 5:
    LEANLAUNCHER_LAUNCH_OPTIONS = leanlauncher_auth_microsoft.leanlauncher_open_auth_microsoft()
  elif choice == 6:
    pass
  elif choice == 7:
    print("Goodbye!")
    exit()



### main program code ###
if __name__ == "__main__":
  while True:
    choice = leanlauncher_main_menu()

    leanlauncher_act_upon_choice(choice)
