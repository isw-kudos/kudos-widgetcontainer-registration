# This will print configuration for all widgets registered. Since the output is large, it is best to output to a file.
# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/printAllWidgets.py > /KudosScriptsDirectory/printAllWidgetsOutput.txt
execfile("newsAdmin.py")
print NewsWidgetCatalogService.browseWidgets()