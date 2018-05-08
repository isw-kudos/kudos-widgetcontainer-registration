# Example usage:
# cd /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/
# ./wsadmin.sh -lang jython -username connectionsadmin -password <YOURPASSWORD> -f /KudosScriptsDirectory/registerBoardsCommWidgets.py <YOUR SERVER FQDN e.g. devconn6.internal.isw.net.au>

execfile("newsAdmin.py")
def registerBoardsCommWidgets():
    try:
        servername = sys.argv[0]
    except IndexError:
        print "Server name not specified. Read this script to see usage."
        return

    boardsContext = "kudosboards" # Change this if you have a different context root than https://servername/kudosboards/
    secureBoardsRoot = "https://"+servername+"/"+boardsContext
    boardsWidgetURL = secureBoardsRoot+"/communityBoards"

    print "\n"
    print "Server name is: "+servername
    print "\n--Registering Widgets-- "
    print boardsWidgetURL
    raw_input("Press ENTER to confirm and continue. CTRL+C to exit.")

    NewsWidgetCatalogService.addWidget( enabled=1, title="Kudos Boards", url=boardsWidgetURL , categoryName="profiles", isHomepageSpecific=0, isDefaultOpened=0, multipleInstanceAllowed=0, isGadget=0, policyFlags=[GadgetPolicyFlags.TRUSTED], prereqs=['profiles','communities','activities'], appContexts=["IWIDGETS"])
    NewsWidgetCatalogService.clearWidgetCaches()

    print "\nAll clusters running IBM Connections applications need to be restarted after registering widgets.\n"

registerBoardsCommWidgets()
