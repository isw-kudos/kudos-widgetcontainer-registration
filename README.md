# kudos-widgetcontainer-registration
Scripts for registering Kudos Communities/Profiles widgets with WidgetContainer. __Applicable to Connections 6 CR1__.

## Resources
[IBM Connections 6.0 CR1 requires all widgets to be registered in the Widget Container](http://www-01.ibm.com/support/docview.wss?uid=swg22011111)

[IBM Knowledge Center - Gadget registration commands - Administering - Connections](https://www.ibm.com/support/knowledgecenter/SSYGQH_6.0.0/admin/admin/r_admin_gadget_reg_ws_commands.html)

[Update Strategy for IBM Connections 6.0](http://www-01.ibm.com/support/docview.wss?uid=swg21999492)

[Updating the IBM Connections 6.0 databases to the required schema versions for Cumulative Refresh 1 (CR1)](http://www-01.ibm.com/support/docview.wss?uid=swg22009306)

## Prerequisites
[IBM Connections 6 CR1 Installed](http://www-01.ibm.com/support/docview.wss?uid=swg21999492)

[IBM Connections 6 CR1 database update scripts run](http://www-01.ibm.com/support/docview.wss?uid=swg22009306)

[Kudos Badges/Analytics v5.0.4+](http://kudosbadges.com/domino/isw/kudos/kudosweb.nsf/downloads/Kudos%20Downloads).

[Kudos Boards v3.0.0+](http://kudosbadges.com/domino/isw/kudos/kudosweb.nsf/downloads/Kudos%20Boards%20Downloads)

## Steps


Copy the files from this repository on to your server. [Download link](https://github.com/isw-kudos/kudos-widgetcontainer-registration/archive/master.zip).

Run each of the appropriate wsadmin scripts (.py) for the Kudos products you have installed. Using your connections admin user.

    ./wsadmin.sh -lang jython -username <USERNAME> -password <PASSWORD> -f /KudosScriptsDirectory/<SCRIPT NAME>.py <YOUR SERVER FQDN>

Example for Kudos Badges:

    ./wsadmin.sh -lang jython -username connectionsadmin -password P@ssw0rd1! -f /KudosScriptsDirectory/registerKudosBadgesWidgets.py connections.isw.net.au

Restart all application servers running Connections applications.

All Kudos Widgets should now be registered and working OK. Test this by opening a Community that has a Kudos widget and a Profiles page.
