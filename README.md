# kudos-widgetcontainer-registration
Scripts for registering Kudos Communities/Profiles widgets with WidgetContainer. __Applicable to Connections 6 CR1__.

## Resources
[IBM Connections 6.0 CR1 requires all widgets to be registered in the Widget Container](http://www-01.ibm.com/support/docview.wss?uid=swg22011111)

[IBM Knowledge Center - Gadget registration commands - Administering - Connections](https://www.ibm.com/support/knowledgecenter/SSYGQH_6.0.0/admin/admin/r_admin_gadget_reg_ws_commands.html)

[Update Strategy for IBM Connections 6.0](http://www-01.ibm.com/support/docview.wss?uid=swg21999492)

[Updating the IBM Connections 6.0 databases to the required schema versions for Cumulative Refresh 1 (CR1)](http://www-01.ibm.com/support/docview.wss?uid=swg22009306)

## Known Issues
Following the IBM provided steps to register widgets Community/Profiles widgets with the WidgetContainer can:
 - make widgets appear in Homepage/My Page widget palette ('Customize' pane)
 - cause the Homepage/My Page widget palette to fail to render and prevent users from adding other widgets to their My Page

IBM have reproduced this in PMR# 40193,756,000.
We have provided a workaround for Kudos widgets included in the _Steps_ section

## Steps
__Kudos Badges/Analytics requires version 5.0.4.__ [Download and install from here](http://kudosbadges.com/domino/isw/kudos/kudosweb.nsf/downloads/Kudos%20Downloads).
This version is expected to be released December 15th (GMT+10).

Copy the files from this repository on to your server. [https://github.com/isw-kudos/kudos-widgetcontainer-registration/archive/master.zip](Download link).

Run each of the appropriate wsadmin scripts (.py) for the Kudos products you have installed. Using your connections admin user.

    `./wsadmin.sh -lang jython -username <USERNAME> -password <PASSWORD> -f /KudosScriptsDirectory/<SCRIPT NAME>.py <YOUR SERVER FQDN>`

Example for Kudos Badges:

    `./wsadmin.sh -lang jython -username connectionsadmin -password P@ssw0rd1! -f /KudosScriptsDirectory/registerKudosBadgesWidgets.py connections.isw.net.au`


To address the known issue above we have written a small SQL query to modify our widgets to be hidden from Homepage the same way IBM have done with their Communities/Profiles widgets. This was derived from the SQL update scrips IBM provided for CR1.

Run the `kudosWidgetsHiddenPane.sql` script against your HOMEPAGE database. This may not be required in the future once the PMR has been resolved.

Restart all application servers running Connections applications.

All Kudos Widgets should now be registered and working OK. Test this by opening a Community that has a Kudos widget and a Profiles page.

Test that your My Page widgets palette is working by clicking 'Customize' in the top right corner of Homepage/My Page.
