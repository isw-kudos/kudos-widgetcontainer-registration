# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/registerKudosBoardsWidgets.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

servername = sys.argv[0]
boardsContext = "kudosboards" # Change this if you have a different context root than https://servername/kudosboards/

http = "http://"
https = "https://"

boardsRoot = http+servername+"/"+boardsContext
secureBoardsRoot = https+servername+"/"+boardsContext

boardsWidgetURL = [boardsRoot+"/communityBoards", secureBoardsRoot+"/communityBoards"]

print "\n"
print "Server name is: "+servername
print "\n--Registering Widgets-- "
print boardsWidgetURL[1]
raw_input("Press ENTER to confirm and continue. CTRL+C to exit.")
execfile("newsAdmin.py")

boards = NewsWidgetCatalogService.addWidget( title="Kudos Boards", url=boardsWidgetURL[0] ,secureUrl=boardsWidgetURL[1], categoryName=WidgetCategories.NONE, isHomepageSpecific=0, isDefaultOpened=0, multipleInstanceAllowed=0, isGadget=0, policyFlags=[GadgetPolicyFlags.TRUSTED], prereqs=['profiles','communities','activities'], appContexts=["EMBEDXP"])
NewsWidgetCatalogService.enableWidget(boards)
NewsWidgetCatalogService.clearWidgetCaches()

print "\nApplication Servers running Homepage need to be restarted after registering widgets.\n"