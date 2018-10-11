# kudos-widgetcontainer-registration
Scripts for registering Kudos Communities/Profiles widgets with WidgetContainer. __Applicable to Connections 6 CR1 onwards__.

## Resources
[IBM Connections 6.0 CR1 onwards requires all widgets to be registered in the Widget Container](http://www-01.ibm.com/support/docview.wss?uid=swg22011111)

[IBM Knowledge Center - Gadget registration commands - Administering - Connections](https://www.ibm.com/support/knowledgecenter/SSYGQH_6.0.0/admin/admin/r_admin_gadget_reg_ws_commands.html)

[Update Strategy for IBM Connections 6.0](http://www-01.ibm.com/support/docview.wss?uid=swg21999492)

[Updating the IBM Connections 6.0 databases to the required schema versions for Cumulative Refresh 1 (CR1)](http://www-01.ibm.com/support/docview.wss?uid=swg22009306)

## Prerequisites
[IBM Connections 6 CR1 or later Installed](http://www-01.ibm.com/support/docview.wss?uid=swg21999492)

[IBM Connections 6 CR1 or later database update scripts run](http://www-01.ibm.com/support/docview.wss?uid=swg22009306)

[Kudos Badges/Analytics v5.0.4+](http://kudosbadges.com/domino/isw/kudos/kudosweb.nsf/downloads/Kudos%20Downloads).

[Kudos Boards v3.0.0+](http://kudosbadges.com/domino/isw/kudos/kudosweb.nsf/downloads/Kudos%20Boards%20Downloads)

## Steps

Ensure the prerequisites above have already been completed/installed.

Copy the files from this repository on to your server. [Download link](https://github.com/isw-kudos/kudos-widgetcontainer-registration/archive/master.zip).

Run each of the appropriate wsadmin scripts (.py) for the Kudos products you have installed. Using your connections admin user.

    ./wsadmin.sh -lang jython -username <USERNAME> -password <PASSWORD> -f /KudosScriptsDirectory/<SCRIPT NAME>.py <YOUR SERVER FQDN>

Example for Kudos Badges:

    ./wsadmin.sh -lang jython -username connectionsadmin -password P@ssw0rd1! -f /KudosScriptsDirectory/registerBadgesProfCommWidgets.py connections.isw.net.au

Restart all clusters running Connections applications.

All Kudos Widgets should now be registered and working OK. Test this by opening a Community that has a Kudos widget and a Profiles page.

## Other Notes
- Widget Registration must be completed for ALL third party widgets. These scripts will only register/update widgets for Kudos products.
If you have widgets from other products (OnTime, XCC, custom/in-house) you will also need to complete similar steps for those products and widgets. You are welcome to adapt the code provided here for other widgets.

- All registered widget URLs must be absolute. These scripts will always register absolute URLs. However, if you're doing your own thing you should know that relative URLs will cause the widgets to fail loading. Check the output of printAllWidgets.py for any relative URLs.

- These scripts will only register https:// URLs. If your widget-config.xml is using relative URLs for these widgets and you access Connections over http:// the widgets will fail to load.

- Your browser can cache the definitions of widgets received from the server even if they are not working. Be sure to test loading the changed widgets without a browser cache whenever the Connections widget cache is cleared. Either by clearing your browser cache or using an incognito/private browsing session.

- This trace string will output detailed logs for the WidgetContainer application: `*=info:com.ibm.cre*=all`
Search for `was not allowed for container` to find the URLs that have not been registered properly.
