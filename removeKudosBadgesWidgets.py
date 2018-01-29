# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/removeKudosBadgesWidgets.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

servername = sys.argv[0]
kudosContext = "Kudos" # Change this if you have a different context root than https://servername/Kudos/

kudosRoot = "http://"+servername+"/"+kudosContext
secureKudosRoot = "https://"+servername+"/"+kudosContext


awardSummaryURL		=		[kudosRoot+"/AwardSummaryDisplay.xml",		secureKudosRoot+"/AwardSummaryDisplay.xml"]
awardViewAllURL		=		[kudosRoot+"/AwardViewAll.xml",				secureKudosRoot+"/AwardViewAll.xml"]
badgeSummaryURL		=		[kudosRoot+"/BadgeSummaryDisplay.xml",		secureKudosRoot+"/BadgeSummaryDisplay.xml"]
badgeViewAllURL		=		[kudosRoot+"/BadgeViewAll.xml",				secureKudosRoot+"/BadgeViewAll.xml"]
thanksSummaryURL	=		[kudosRoot+"/ThanksSummaryDisplay.xml",		secureKudosRoot+"/ThanksSummaryDisplay.xml"]
thanksViewAllURL	=		[kudosRoot+"/ThanksViewAll.xml",			secureKudosRoot+"/ThanksViewAll.xml"]
profileProgressURL	=		[kudosRoot+"/ProfileProgress.xml",			secureKudosRoot+"/ProfileProgress.xml"]
commLeaderboard		=		[kudosRoot+"/CommunityRankingDisplay.xml",	secureKudosRoot+"/CommunityRankingDisplay.xml"]
badgesConfigURL		=		[kudosRoot+"/BadgesConfigurator.xml",		secureKudosRoot+"/BadgesConfigurator.xml"]
filtersConfigURL	=		[kudosRoot+"/FiltersConfigurator.xml",		secureKudosRoot+"/FiltersConfigurator.xml"]
metricsConfigURL	=		[kudosRoot+"/MetricsConfigurator.xml",		secureKudosRoot+"/MetricsConfigurator.xml"]

print "\n"
print "Server name is: "+servername
print "\n--REMOVING Widgets-- "
print awardSummaryURL[0]
print awardViewAllURL[0]
print badgeSummaryURL[0]
print badgeViewAllURL[0]
print thanksSummaryURL[0]
print thanksViewAllURL[0]
print profileProgressURL[0]
print commLeaderboard[0]
print badgesConfigURL[0]
print filtersConfigURL[0]
print metricsConfigURL[0]
raw_input("Press ENTER to confirm and continue. CTRL+C to exit.")
execfile("newsAdmin.py")

NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(awardSummaryURL[0])["widgetId"])
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(awardViewAllURL[0])["widgetId"])
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(badgeSummaryURL[0])["widgetId"])
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(badgeViewAllURL[0])["widgetId"])
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(thanksSummaryURL[0])["widgetId"])
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(thanksViewAllURL[0])["widgetId"])
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(profileProgressURL[0])["widgetId"])
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(commLeaderboard[0])["widgetId"])
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(badgesConfigURL[0])["widgetId"])
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(filtersConfigURL[0])["widgetId"])
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl(metricsConfigURL[0])["widgetId"])
NewsWidgetCatalogService.clearWidgetCaches()

print "\nAll IBM Connections application servers need to be restarted after registering widgets.\n"
