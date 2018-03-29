# This will print configuration for all widgets registered.
# If you only have one server for the News service, the output can be written to a file as in the example.
# With multiple servers, you'll need to enter numbers for the service to connect to.
# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/printAllWidgets.py > /KudosScriptsDirectory/printAllWidgetsOutput.txt
execfile("newsAdmin.py")
print NewsWidgetCatalogService.browseWidgets()
