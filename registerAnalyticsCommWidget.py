# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/registerAnalyticsCommWidget.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

execfile("newsAdmin.py")
def registerAnalyticsCommWidget():
    try:
        servername = sys.argv[0]
    except IndexError:
        print "Server name not specified. Read this script to see usage."
        return

    kudosContext = "Kudos" # Change this if you have a different context root than https://servername/Kudos/
    secureKudosRoot = "https://"+servername+"/"+kudosContext
    analyticsWidgetURL = secureKudosRoot+"/AnalyticsDashboard.xml"

    print "\n"
    print "Server name is: "+servername
    print "\n--Registering Widgets-- "
    print analyticsWidgetURL
    raw_input("Press ENTER to confirm and continue. CTRL+C to exit.")

    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Analytics",	url=analyticsWidgetURL,	categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=1,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles', 'communities'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.clearWidgetCaches()

    print "\nAll clusters running IBM Connections applications need to be restarted after registering widgets.\n"
registerAnalyticsCommWidget()
