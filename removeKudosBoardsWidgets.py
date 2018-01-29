# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/removeKudosBoardsWidgets.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

servername = sys.argv[0]
boardsContext = "kudosboards" # Change this if you have a different context root than https://servername/kudosboards/

boardsRoot = "http://"+servername+"/"+boardsContext
secureBoardsRoot = "https://"+servername+"/"+boardsContext

boardsWidgetURL = [boardsRoot+"/communityBoards", secureBoardsRoot+"/communityBoards"]

print "\n"
print "Server name is: "+servername
print "\n--REMOVING Widgets-- "
print boardsWidgetURL[0]
raw_input("Press ENTER to confirm and continue. CTRL+C to exit.")
execfile("newsAdmin.py")

NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(boardsWidgetURL[0])["widgetId"])
NewsWidgetCatalogService.clearWidgetCaches()

print "\nAll IBM Connections application servers need to be restarted after registering widgets.\n"
