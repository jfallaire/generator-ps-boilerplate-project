.. _ui_custo:

UI Customizations
=================

This section of the documentation regroups topics describing various customizations made during this implementation to meet requirements that were not specifically available in the OOTB UI components of Coveo.

Before going further we highly recommend you get yourself familiar with the `JS Search framework of Coveo`_.

Adding Customizations to Lightning Components
---------------------------------------------

Any UI customizations must be added through the *customScripts* attribute on the lightning Coveo component inside the different wrapper lightning components used for this implementation. 
The wrapper is also a clean way to further customize your integration to your specific needs.

Using this appoach allows you to fully customize your wrapper component using Coveo component:

  * You can include your javascript custom code using Static Resource
  * You can fully customized the result templates
  * full control on CSS stylesheet.

<%=customerSafeName%> bundle assets
*********************

The javascript bundle (``<%=customerSafeName%>.bundle.js``) made for this implementation is an extension ( a complement ) of the Coveo JavaScript Search Framework that must be included as part of the different lightning components ( as ``customScripts`` attribute)  
used for the <%=customerSafeName%>'s implementation. Adding this bundle allows to use custom UI components ( see `Custom Components`_  below ) inside your Search interface HTML Markup and/or result templates.

You will retrieve this bundle along with the different culture files into the following Salesforce static resource (contentType: ``application/zip``) : ``<%=customerSafeName%>_bundle_assets`` 

.. code::

    <%=customerSafeName%>_bundle_assets
      └── js
          ├── cultures
          │   ├── en.js
          │   ├── es-es.js
          │   └── fr.js
          ├── <%=customerSafeName%>.bundle.js
          └── <%=customerSafeName%>.bundle.min.js

Result Templates
****************

.. important:: Since this implementation is being done into a lightning community and because of the way LockerService works, Underscore templates cannot be used. 
                All result templates used during this implementation are using HTML template (see `Result Templates`_ and `HTML Result Template`_)

<%=customerSafeName%> implementation supports four different result templates based on the following field value conditions

.. code-block:: HTML

  ...
  <div class='CoveoResultList'>
    <script id="Knowledge" class="result-template" type="text/html" data-layout="list" data-field-sfkbid="">
        // [ ... ] Result template code for kb [ ... ]
    </script>

    <script id="YtPlaylist" class="result-template" type="text/html" data-layout="list" data-field-ytplaylistid="">
        // [ ... ] Result template code for youtube playlist [ ... ]
    </script>

    <script id="YtVideo" class="result-template" type="text/html" data-layout="list" data-field-ytvideoid="">
        // [ ... ] Result template code for youtube video [ ... ]
    </script>

    <script id="Default" class="result-template" type="text/html" data-layout="list">
        // [ ... ] Result template code [ ... ]
    </script>
  </div>
  ...

Knowledge
+++++++++

The markup for ``kb`` HTML result template look like this:

.. literalinclude:: ../../views/templates/community/kb.ejs
  :linenos:

Visually, this result template would look like this:

.. image:: ../_static/img/<%=customerSafeName%>_result_kb.png

Youtube Playlist
++++++++++++++++

The markup for ``YtPlaylist`` HTML result template look like this:

.. literalinclude:: ../../views/templates/community/ytplaylist.ejs
  :linenos:

Visually, this result template would look like this:

.. image:: ../_static/img/<%=customerSafeName%>_result_ytplaylist.png

Youtube Video
+++++++++++++

The markup for ``YtVideo`` HTML result template look like this:

.. literalinclude:: ../../views/templates/community/ytvideo.ejs
  :linenos:

Visually, this result template would look like this:

.. image:: ../_static/img/<%=customerSafeName%>_result_ytvideo.png

Default
+++++++

The markup for ``default`` HTML result template look like this:

.. literalinclude:: ../../views/templates/community/default.ejs
  :linenos:

Visually, this result template would look like this:

.. image:: ../_static/img/<%=customerSafeName%>_result_default.png

Search Interfaces
*****************

Two different search interface partials have been created to meet <%=customerSafeName%> requirements. These partials contain the configuration of each component (custom ones included, see `Custom Components`_) through the HTML markup.
They are located in the ``./views/partials`` folder and are used by the webpack configuration to auto-generate the Visualforce Components required by the different lightning components made for this implementation.

There is one used for the Search page itself and the other one is used for the different Case Deflection pages. All of them are using the same result templates composition in order to keep consistency across the different possible search entry point. (refer to above `Result Templates`_ section)

 
Custom Localized Strings
************************

This implementation supports 3 different cultures (english, french and spanish) that you can retrieve as part of the ``<%=customerSafeName%>_bundle_assets`` static resource (under ``./js/culture``).
The javascript <%=customerSafeName%> bundle (see ``./src/typescripts/CoveoCustomScripts.ts``) ensures ``String.locale`` match the current locale on community and also ensures to set custom language dictionary properly for lightning community, thus the fact we need to define ``setCustomLanguageDict`` in different custom culture files.

.. literalinclude:: ../../src/typescripts/cultures/en.js
    :language: javascript
    :linenos:
    :caption: Example: Localized Strings for english

In lightning, a custom setting has been used to handle the different cultures/languages supported at <%=customerSafeName%>. It's also used to dynamically inject the appropriate culture files (OOTB + custom) as part of the ``customScripts`` attribute.

.. literalinclude:: ../../force-app/main/default/aura/VLC_Coveo_CommunitySearch/VLC_Coveo_CommunitySearch.cmp
    :language: HTML
    :linenos:
    :emphasize-lines: 13-16


What's next?
************

You should now proceed and have a look at the different `Custom Components`_ made during for this implementation.

Custom Components
-----------------

.. _ui-custo:

.. toctree::
   :maxdepth: 3

   ui-components/SalesforceCommunityResultLink

.. _JS Search framework of Coveo: https://docs.coveo.com/en/361/javascript-search-framework/javascript-search-framework-getting-started-tutorial
.. _Events: https://docs.coveo.com/en/417/javascript-search-framework/events
.. _Result Templates: https://docs.coveo.com/en/413/
.. _HTML Result Template: https://docs.coveo.com/en/377/

