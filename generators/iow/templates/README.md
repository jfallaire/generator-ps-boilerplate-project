# <%=customerSafeName%>-iow
<%=customerSafeName%>'s IOW 

This project is meant as a working starting point for creating the IOW documentation for <%=customerSafeName%>.

## Build
To Build the whole documentation and generate its output in the `./_build` folder.

    sphinx-autobuild -b html . _build/html

On a mac machine you can also use this command 

    make livehtml

this generates the doc in subfolder _build/html - a beautiful website based on your rst files
this start a local node.js server that will host said site on port 8000
(optional) If for some reason port 8000 isn't to your liking, you can always start this process without the batch file by executing this:
sphinx-autobuild --port 8001 -b html . _build/html
Where 8001 can of course be any port you wish. 
Browse http://127.0.0.1:8000