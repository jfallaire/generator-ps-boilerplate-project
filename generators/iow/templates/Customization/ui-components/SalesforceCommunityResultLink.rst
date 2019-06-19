SalesforceCommunityResultLink
=============================

.. highlight:: html

The ``SalesforceCommunityResultLink`` component automatically transform a community search result title into a clickable link pointing to the proper item in the community.
If result does not match any supported objects defined into his internal url rewriter the component simply acts as a normal ``ResultLink``. Below are the objects supported by the url rewriter :

  * Case
  * FeedItem/FeedComment (Feed vs Question)
  * CollaborationGroup
  * ContentVersion
  * Idea
  * Knowledge Base

Sample Usage
------------

.. admonition:: Examples

    .. literalinclude:: ../../../views/templates/community/kb.ejs
        :lines: 6
        :caption: SalesforceCommunityResultLink sample usage
        :dedent: 8

    .. literalinclude:: ../../../views/templates/community/kb.ejs
        :linenos:
        :caption: Example from ``views/templates/community/kb.ejs``
        :emphasize-lines: 5

Component Options
-----------------


enableUrlRewriter
*****************

.. attribute:: enableUrlRewriter : boolean

Specifies whether to activate the url rewriter meant for lightning community.

Default value is true.

*HTML markup configuration example(s)*

.. code-block:: html
    
    data-enable-url-rewriter='true'
    data-enable-url-rewriter='false'

enableLanguage
**************

.. attribute:: enableLanguage : boolean

Specifies whether to add culture code language to the url (ex: `?language=en_US`)

Default value is false.

*HTML markup configuration example(s)*

.. code-block:: html
    
    data-enable-language='true'
    data-enable-language='false'


useAsPrintable
**************

.. attribute:: useAsPrintable : boolean

Specifies whether the component should display the community URI instead of the specified field.

Default value is false.

*HTML markup configuration example(s)*

.. code-block:: html
    
    data-use-as-printable='true'
    data-use-as-printable='false'

.. attribute:: name : string

Specifies the name of the community. When not specified, the component will try to automatically detect the community name.

Default value is empty string.

*HTML markup configuration example(s)*

.. code-block:: html
    
    data-name='your_community'

.. attribute:: hostname : string

Specifies the hostname of the community. Default value is ``window.location.hostname``.

*HTML markup configuration example(s)*

.. code-block:: html
    
    data-hostname='your_hostname'

.. attribute:: protocol : string

Specifies the protocol of the community. Default value is ``window.location.protocol``.

*HTML markup configuration example(s)*

.. code-block:: html
    
    data-protocol='https'

Component Methods
-----------------

getCommunityName
****************

.. method:: getCommunityName(options: ISalesforceCommunityResultLinkOptions): string

This *static* method gets the community name. Automatically detecting the community name if applicable.

Parameters
    * ``options: ISalesforceCommunityResultLinkOptions`` -- *options for the SalesforceCommunityResultLink*

Returns the community name

getCommunityUrl
***************

.. method:: getCommunityUrl(result: Coveo.IQueryResult, options:ISalesforceCommunityResultLinkOptions) : string

This *static* method gets the community url for the given result.

Parameters
  * ``result: Coveo.IQueryResult`` -- *Coveo Result*
  * ``options: ISalesforceCommunityResultLinkOptions`` -- *options for the SalesforceCommunityResultLink*

Returns the current community url

