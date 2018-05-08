# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/registerBadgesProfCommWidgets.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

execfile("newsAdmin.py")

def registerBadgesProfCommWidgets():
    try:
        servername = sys.argv[0]
    except IndexError:
        print "Server name not specified. Read this script to see usage."
        return
    kudosContext = "Kudos" # Change this if you have a different context root than https://servername/Kudos/

    secureKudosRoot = "https://"+servername+"/"+kudosContext

    awardSummaryURL		=		secureKudosRoot+"/AwardSummaryDisplay.xml"
    awardViewAllURL		=		secureKudosRoot+"/AwardViewAll.xml"
    badgeSummaryURL		=		secureKudosRoot+"/BadgeSummaryDisplay.xml"
    badgeViewAllURL		=		secureKudosRoot+"/BadgeViewAll.xml"
    thanksSummaryURL	=		secureKudosRoot+"/ThanksSummaryDisplay.xml"
    thanksViewAllURL	=		secureKudosRoot+"/ThanksViewAll.xml"
    profileProgressURL	=		secureKudosRoot+"/ProfileProgress.xml"
    commLeaderboard		=		secureKudosRoot+"/CommunityRankingDisplay.xml"
    badgesConfigURL		=		secureKudosRoot+"/BadgesConfigurator.xml"
    filtersConfigURL	=		secureKudosRoot+"/FiltersConfigurator.xml"
    metricsConfigURL	=		secureKudosRoot+"/MetricsConfigurator.xml"

    print "\n"
    print "Server name is: "+servername
    print "\n--Registering Widgets-- "
    print awardSummaryURL
    print awardViewAllURL
    print badgeSummaryURL
    print badgeViewAllURL
    print thanksSummaryURL
    print thanksViewAllURL
    print profileProgressURL
    print commLeaderboard
    print badgesConfigURL
    print filtersConfigURL
    print metricsConfigURL
    raw_input("Press ENTER to confirm and continue. CTRL+C to exit.")

    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Awards Summary",			url=awardSummaryURL,	 categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Awards",					url=awardViewAllURL,	 categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Badges Summary",			url=badgeSummaryURL,	 categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Badges",					url=badgeViewAllURL,     categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Thanks Summary",			url=thanksSummaryURL,	 categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Thanks",					url=thanksViewAllURL,	 categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Profile Progress",			url=profileProgressURL,  categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Community Leaderboard",	url=commLeaderboard,	 categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles', 'communities'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Badges Configurator",		url=badgesConfigURL,	 categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles', 'communities'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Filters Configurator",		url=filtersConfigURL,	 categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles', 'communities'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.addWidget(   enabled=1,	title="Kudos Metrics Configurator",		url=metricsConfigURL,	 categoryName="profiles", isHomepageSpecific=0,	isDefaultOpened=0,	multipleInstanceAllowed=0,	isGadget=0,	policyFlags=[GadgetPolicyFlags.TRUSTED], 	prereqs=['profiles', 'communities'],	appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.clearWidgetCaches()

    print "\nAll clusters running IBM Connections applications need to be restarted after registering widgets.\n"
registerBadgesProfCommWidgets()
