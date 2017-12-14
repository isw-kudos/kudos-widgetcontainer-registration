# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/registerKudosAnalyticsWidgets.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

servername = sys.argv[0]
kudosContext = "Kudos" # Change this if you have a different context root than https://servername/Kudos/

http = "http://"
https = "https://"

kudosRoot = http+servername+"/"+kudosContext
secureKudosRoot = https+servername+"/"+kudosContext

analyticsWidgetURL = [kudosRoot+"/AnalyticsDashboard.xml", secureKudosRoot+"/AnalyticsDashboard.xml"]

print "\n"
print "Server name is: "+servername
print "\n--Registering Widgets-- "
print analyticsWidgetURL[1]
raw_input("Press ENTER to confirm and continue. CTRL+C to exit.")
execfile("newsAdmin.py")

 
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Analytics",	url=analyticsWidgetURL[0],	secureUrl=analyticsWidgetURL[1],	categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=1,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles', 'communities'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.clearWidgetCaches()

print "\nApplication Servers running Homepage need to be restarted after registering widgets.\n"