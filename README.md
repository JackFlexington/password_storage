# Password Storage
Graphical User Interface made with tkinter... Database management is handled via SQLite.

## Release
v0.1 "BETA" for use-case testing.

## What you'll need to do in order to run these programs
1. Clone Repository to local machine
    * I use Visual Studio to clone && commit to remote repository's
2. tkinter is native to any recent Python installation... [head over to Python.org](https://www.python.org/downloads/) for the latest Python release.
3. Feed "passwordstorage.py" into locally installed Python
    * Open up "CMD" (Windows) or "Terminal" (Apple / Linux)... Navigate to the directory where repo was cloned and key in one of the following lines of text. 
    * Example #1: ```py passwordstorage.py```
    * Example #2: ```python passwordstorage.py```
    * Example #3: ```python3 passwordstorage.py```
4. If done successfully you should should see the command prompt with a few consoles messages, as well as the graphical user interface for "Password Storage".

## Known Issues
### Logic Errors
~~1. UNIQUE row id gets removed in the SQLite database via GUI button "Remove Entry".
    * Primary issue: When attempting to add new rows AFTER removing an existing one, the database chokes due to row ID not being UNIQUE. 
      * Row ID is currently getting determined based on the number of rows shown in the GUI display window.~~
  * Corrected above issue.
