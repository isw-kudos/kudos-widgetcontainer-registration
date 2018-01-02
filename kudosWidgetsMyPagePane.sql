--This script will undo the change made with kudosWidgetsHiddenPane.sql. It sets all of the mentioned widgets to be available on My Page.
UPDATE HOMEPAGE.HP_WIDGET_TAB SET TAB_ID = '_panel.widgetx4a43x82aaxb00187218631'
WHERE WIDGET_ID IN (
	SELECT WIDGET_ID
	FROM HOMEPAGE.WIDGET
	WHERE 
		WIDGET_URL LIKE '%AnalyticsDashboard.xml' OR
		WIDGET_URL LIKE '%AwardSummaryDisplay.xml' OR
		WIDGET_URL LIKE '%AwardViewAll.xml' OR
		WIDGET_URL LIKE '%BadgesConfigurator.xml' OR
		WIDGET_URL LIKE '%BadgeSummaryDisplay.xml' OR
		WIDGET_URL LIKE '%BadgeViewAll.xml' OR
		WIDGET_URL LIKE '%CommunityRankingDisplay.xml' OR
		WIDGET_URL LIKE '%FiltersConfigurator.xml' OR
		WIDGET_URL LIKE '%MetricsConfigurator.xml' OR
		WIDGET_URL LIKE '%ProfileProgress.xml' OR
		WIDGET_URL LIKE '%ThanksSummaryDisplay.xml' OR
		WIDGET_URL LIKE '%ThanksViewAll.xml' OR
		WIDGET_URL LIKE '%/communityBoards'
)