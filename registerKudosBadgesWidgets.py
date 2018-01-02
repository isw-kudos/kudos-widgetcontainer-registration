# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/registerKudosBadgesWidgets.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

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
print "\n--Registering Widgets-- "
print awardSummaryURL[1]
print awardViewAllURL[1]
print badgeSummaryURL[1]
print badgeViewAllURL[1]
print thanksSummaryURL[1]
print thanksViewAllURL[1]
print profileProgressURL[1]
print badgesConfigURL[1]
print filtersConfigURL[1]
print metricsConfigURL[1]
raw_input("Press ENTER to confirm and continue. CTRL+C to exit.")
execfile("newsAdmin.py")


NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Awards Summary",			url=awardSummaryURL[0],		secureUrl=awardSummaryURL[1],		 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Awards",					url=awardViewAllURL[0],		secureUrl=awardViewAllURL[1],		 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Badges Summary",			url=badgeSummaryURL[0],		secureUrl=badgeSummaryURL[1],		 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Badges",					url=badgeViewAllURL[0],		secureUrl=badgeViewAllURL[1],		 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Thanks Summary",			url=thanksSummaryURL[0],	secureUrl=thanksSummaryURL[1],		 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Thanks",					url=thanksViewAllURL[0],	secureUrl=thanksViewAllURL[1],		 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Profile Progress",			url=profileProgressURL[0],	secureUrl=profileProgressURL[1],	 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Community Leaderboard",	url=commLeaderboard[0],		secureUrl=commLeaderboard[1],		 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles', 'communities'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Badges Configurator",		url=badgesConfigURL[0],		secureUrl=badgesConfigURL[1],		 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles', 'communities'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Filters Configurator",		url=filtersConfigURL[0],	secureUrl=filtersConfigURL[1],		 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles', 'communities'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.enableWidget(NewsWidgetCatalogService.addWidget(	title="Kudos Metrics Configurator",		url=metricsConfigURL[0],	secureUrl=metricsConfigURL[1],		 categoryName=WidgetCategories.NONE, isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles', 'communities'],	appContexts=["EMBEDXP"]))
NewsWidgetCatalogService.clearWidgetCaches()

print "\nApplication Servers running Homepage need to be restarted after registering widgets.\n"
