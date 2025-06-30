Copyright 2025, Michael Griffiths

This file is part of npdf aka "Natural PDF".
npdf is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
npdf is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with npdf. If not, see <https://www.gnu.org/licenses/>.

*Description:*

Creates a PDF from a folder or directory with image files in it.  The resulting PDF file will be named after the foldername.

*Pre-requisites:*

Python 3.x

*General Build Instructions:*

1. Clone this repo:

```
git clone https://github.com/griffmick/npdf && cd npdf
```

2. Activate your Python virtual environment:

```
python -m venv .venv && source .venv/bin/activate
```

3. Install the pre-requisite import modules:

```
pip install -r requirements.txt
```

4. Freeze the stuff as a self contained binary and deactivate your Python virtual environment:

```
pyinstaller -F npdf.py && deactivate
```

5. Pray that it doesn't get any harder than copying the dist/npdf executable to somewhere usable (/usr/local/bin, or maybe even on your $PATH).

```
sudo cp dist/npdf /usr/local/bin/npdf
```

6. Contribute something to open source and use a fun operating system!

*Usage:*
Create a directory/folder with the name of the PDF you want to create, and fill it with the images you want.  Then run the npdf command from that folder location.  Simple!

```
cd 'my_folder_full_of_images'
npdf
```
