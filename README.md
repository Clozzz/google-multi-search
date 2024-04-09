This is a simple script that runs against Google's Search API and searches for a given query's Terms of Service and Privacy Policy outputting results to the terminal
to be further examined. In order to run the script it is recommended to create a virtual environment before installing the requests library that is need in order to
run the script. This can be done with:

```
python3 -m venv NAME_OF_DIRECTORY
```

Once the virtual environment has been created you must activate it in your shell before the environment can be utilized this is achieved with:

```
source NAME_OF_DIRECTORY/bin/activate
```
Inside of your terminal.

Once the virtual environment is active you can install the requests library needed for the script to function with:

```
pip install requests
```

This will install the requests library and will allow execution of the script.

Before the script can run properly you will need to procure two items:
1. A Google Programmable Search API Key: https://developers.google.com/custom-search/v1/overview
    - If you're logged in you should see the option to generate an API key
    - Once you have your key make sure to keep it private
2. A Google Programmable Search Engine: https://programmablesearchengine.google.com/controlpanel/create
    - Name your search engine whatever you like e.g. "tos-privpol-search"
    - While not required it is recommended to turn safe search on
    - Confirm you are no robo and click "create"
    - Store your information and then hit continue to get to where you can see your engine ID
    - Copy engine ID into script

From here simply invoke python and the script itself with:

```
python3 request.py
```
Once the script begins to run it will request a string for the search query, it is recommended to enter the name of the company and, should the company
be somewhat obscure, potentially some additional identifiers. This script is ultimately taking some very simple actions - running a search query against
a Google API and returning results, but running three searches at a time should hopefully be a time saver.
