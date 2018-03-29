# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/removeAnalyticsProfCommWidgets.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

execfile("newsAdmin.py")

def removeAnalyticsCommWidget():
    try:
        servername = sys.argv[0]
    except IndexError:
        print "Server name not specified. Read this script to see usage."
        return

    kudosContext = "Kudos" # Change this if you have a different context root than https://servername/Kudos/
    secureKudosRoot = "https://"+servername+"/"+kudosContext

    widgetUrls = []
    widgetUrls.append(secureKudosRoot+"/AnalyticsDashboard.xml")

    print "\n"
    print "Server name is: "+servername
    print "\n--REMOVING Widgets-- "
    for widgetUrl in widgetUrls:
        print widgetUrl
    raw_input("Press ENTER to confirm and continue. CTRL+C to exit.")

    for widgetUrl in widgetUrls:
        widget = NewsWidgetCatalogService.findWidgetByUrl(widgetUrl);
        if not widget:
            print "Widget not found for url: " + widgetUrl
        else:
            NewsWidgetCatalogService.removeWidget(widget["widgetId"])
            print "SUCCESS: " + widgetUrl

    NewsWidgetCatalogService.clearWidgetCaches()

    print "\nAll clusters running IBM Connections applications need to be restarted after registering widgets.\n"

removeAnalyticsCommWidget()
