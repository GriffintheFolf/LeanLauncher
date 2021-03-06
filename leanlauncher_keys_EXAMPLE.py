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

"""
This file contains client secrets used for authentication with Microsoft Azure.

If you are basing your own launcher off this code, you must copy or rename this
file to leanlauncher_keys.py.
Be sure to set the keys to your own Azure application, otherwise it will be
useless.

Furthermore, you MUST ensure that the keys are stored in such a way that they
will not be easily accessible by a wouldbe attacker.
"""

# Set this to the client ID given by Azure
LEANLAUNCHER_CLIENT = ""

# Set this to the secret given by Azure
LEANLAUNCHER_SECRET = ""

# Set this to your redirect URI
LEANLAUNCHER_REDIRECT_URI = ""
