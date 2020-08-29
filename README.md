# COUCHCMS-INTELLISENSE

## FEATURES

This VSCode extension adds support for CouchCMS custom HTML tags. Gives VSCode the ability to autocomplete tags, parameters, and values. Also will show the documentation as well as examples when triggering suggestions (Ctrl + Space). If the detailed info isn't showing when triggering suggestions, press the (Ctrl + Space) again to show more info.

## INSTALLING

There are a few methods of using this code.

1. Go to [html.html-data.json](html.html-data.json) copy and paste this into a new file in your workspace .vscode directory with the same name. Then press (Ctrl + ,) or open your settings and find HTML Custom Data. Find where it is asking for "A list of relative file paths pointing to JSON files following the custom data format." If you named the file html.html-data.json and put this file in the .vscode directory then click "Add Item" and enter ".vscode/html.html-data.json" 

2. You can clone this repo and then either open the directory you cloned this with VSCode or change directory in your command line to where you cloned this and type "code ." to open the repo in VSCode. Once there head to the debug section and click run extension.

3. (Recommended) Open VSCode and search for and install the extension "CouchCMS Intellisense". This method is the easiest and most permanent. Meaning you only have to do this a single time and it'll be good any time you open up VSCode unlike as with the other methods(1 and 2) where any new project/workspace you'll need to repeat process.

## TROUBLESHOOTING

If you're having trouble getting the autocompletion or hover to work, make sure your settings are allowing customData suggestions. Also be sure the file's language is set to HTML in the bottom right of the window.

See https://github.com/microsoft/vscode-custom-data