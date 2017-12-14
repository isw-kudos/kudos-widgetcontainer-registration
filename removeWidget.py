# This is an example for how you can remove a widget using wsadmin

execfile("newsAdmin.py")
NewsWidgetCatalogService.removeWidget(NewsWidgetCatalogService.findWidgetByUrl("http://devconn6.internal.isw.net.au/Kudos/CommunityRankingDisplay.xml")["widgetId"])
NewsWidgetCatalogService.clearWidgetCaches()