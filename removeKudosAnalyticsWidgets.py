# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/removeKudosAnalyticsWidgets.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

servername = sys.argv[0]
kudosContext = "Kudos" # Change this if you have a different context root than https://servername/Kudos/

kudosRoot = "http://"+servername+"/"+kudosContext
secureKudosRoot = "https://"+servername+"/"+kudosContext

analyticsWidgetURL = [kudosRoot+"/AnalyticsDashboard.xml", secureKudosRoot+"/AnalyticsDashboard.xml"]

print "\n"
print "Server name is: "+servername
print "\n--REMOVING Widgets-- "
print analyticsWidgetURL[0]
raw_input("Press ENTER to confirm and continue. CTRL+C to exit.")
execfile("newsAdmin.py")


NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(analyticsWidgetURL[0])["widgetId"])
NewsWidgetCatalogService.clearWidgetCaches()

print "\nAll IBM Connections application servers need to be restarted after registering widgets.\n"
