UPDATE HOMEPAGE.HP_WIDGET_TAB SET TAB_ID = '_noui.iwidgetpanx11e1b0c40800200c9a6'
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