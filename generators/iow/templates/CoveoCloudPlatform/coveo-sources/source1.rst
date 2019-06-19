********
Source 1
********
.. role:: cloud
    :class: coveo-cloud-badge bg-azure

Source Type
===========

* Sitemap :cloud:`Cloud`

Basic Configuration
===================

URL(s):
    - Your_URL

User agent:
    * ``googlebot``
  
.. warning:: User agent ``googlebot`` is required so we can index a ‘static’ HTML view of every page in your community. For further information, see `Advanced SEO for lightning Communities`_

Security:
    * Shared

Web Scraping Configuration
==========================

.. note:: The web scraping configuration below will help to improve relevancy of the indexed content. It will clean up the html body by removing unwanted sections such as footer, print, noscript, etc... 

.. code-block:: json

    [
      {
        "for": {
          "urls": [
            ".*"
          ]
        },
        "exclude": [
          {
            "type": "CSS",
            "path": "#auraAppcacheProgress"
          },
          {
            "type": "CSS",
            "path": "#auraLoadingBox"
          },
          {
            "type": "CSS",
            "path": "#auraErrorMask"
          },
          {
            "type": "CSS",
            "path": "div[data-region-name=\"customHeader\"]"
          },
          {
            "type": "CSS",
            "path": "#footer"
          }
        ],
        "metadata": {
          "langLocale": {
            "type": "XPATH",
            "path": "//html/@lang"
          }
        }
      }
    ]

Pre-Conversion Extensions
==========================

.. note:: Sequence order below is important


* :ref:`reject_document`
  
  * exclusion_rules: ``[\"(?i).*/s/(contactsupport|livechat|article).*\"]``

* :ref:`set_locale`
   
Configuration Files
===================

* :download:`Field Mappings JSON <../../Downloads/sources/source1_mappings.json>`
* :download:`Pre-Conversion Extensions JSON <../../Downloads/sources/source1_pre_extensions.json>`
* :download:`All Configuration JSON <../../Downloads/sources/source1_all.json>`


.. _Advanced SEO for lightning Communities: https://developer.salesforce.com/blogs/2018/01/advanced-seo-lightning-communities.html
