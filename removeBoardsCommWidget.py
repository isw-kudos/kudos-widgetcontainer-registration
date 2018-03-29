# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/removeAnalyticsProfCommWidgets.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

execfile("newsAdmin.py")

def removeBoardsCommWidget():
    try:
        servername = sys.argv[0]
    except IndexError:
        print "Server name not specified. Read this script to see usage."
        return

    widgetUrls = []
    boardsContext = "kudosboards" # Change this if you have a different context root than https://servername/kudosboards/
    widgetUrls.append("https://"+servername+"/"+boardsContext+"/communityBoards")

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

removeBoardsCommWidget()
