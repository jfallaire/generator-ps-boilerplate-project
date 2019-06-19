.. _Deployment_sfdc_deployment:

***************************
Salesforce Deployment Guide
***************************

This deployment guide is meant to supplements (not to replace) Coveo’s Online Help and Coveo Administrator Training in helping administrators 
and developers to configure, maintain, debug, customize and install/restore the Coveo implementation performed at <%=customerSafeName%> by 
Coveo Professional Services. 



Pre-Deployment Steps
====================

Coveo Cloud Platform
--------------------

.. note::
    This step will be handled by Coveo Professional Services during your initial deployment.

    * Configure the org in the Coveo Cloud (Sources, fields, pipelines, etc.)

Coveo for Salesforce
--------------------
    * Identify your Salesforce target environment where you want to perform your deployment. See the :ref:`Overview_salesforce_orgs` section for more information on the installed versions
        - If the target environment doesn't have Coveo for Salesforce V2 installed, your must install it first;
    * Perform the installation of the package as described in the Coveo Online documentation
        - See `Installing the Coveo for Salesforce V2 Application <https://onlinehelp.coveo.com/en/cloud/Installing_the_Coveo_for_Salesforce_V2_Application.htm>`_
    * Link your Coveo for Salesforce package with your Coveo cloud platform target organization
        - Identify your Coveo target org. See the :ref:`Overview_coveo_orgs` section
        - See `Provisioning the Coveo for Salesforce V2 Application <https://onlinehelp.coveo.com/en/cloud/Provisioning_the_Coveo_for_Salesforce_V2_Application.htm>`_

.. important::
    
    If the target environment has a previous version of Coveo for Salesforce V2 installed, you might want to upgrade your package to the same version 
    as the one installed in the source environment. When upgrading the Coveo for Salesforce V2 application: 
    review the release notes (see `Coveo for Salesforce V2 - Release Notes <https://developers.coveo.com/x/OICpAQ>`_).


Deployment
==========
In order to facilitate the deployment we highly recommend to create an outbound changeset from the source environment (*Full Sandbox*) gathering all the different custom pages/components/etc made for this implementation. 
Below is the list of all the Salesforce objects we have created and/or modified during this project. 

<%=customerSafeName%> custom components
-----------------------

:download:`package.xml <../../manifest/package.xml>`

+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
|                            *Name*                            |    *Object Type*     |                                                      *Description*                                                      |
+==============================================================+======================+=========================================================================================================================+
| VLC_Coveo_CommunitySearchController                          | ApexClass            | Controller used to generate a filter expression based on user profile.                                                  |
|                                                              |                      | It is also used to provide contextual information.                                                                      |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| VLC_Coveo_CommunitySearchControllerTest                      | ApexClass            | Test Class                                                                                                              |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| VLC_Coveo_EndpointHandlerController                          | ApexClass            | Controller used to generate custom search token based on user profile.                                                  |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| VLC_Coveo_EndpointHandlerControllerTest                      | ApexClass            | Test Class                                                                                                              |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| VLC_Coveo_CommunityCaseDeflection                            | AuraDefinitionBundle | Represents the suggested articles (Case deflection) component                                                           |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| VLC_Coveo_CommunitySearch                                    | AuraDefinitionBundle | Represents the community search component.                                                                              |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| VLC_Coveo_CommunitySearchBox                                 | AuraDefinitionBundle | Represents the community search box component                                                                           |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| VLC_Coveo_CreateCaseEvent                                    | AuraDefinitionBundle | Represents Create Case event used to notify Case deflection component.                                                  |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| VLC_Coveo_EndpointHandler                                    | AuraDefinitionBundle | This component allows you to generate the appropriate search token based on profile user                                |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>SupportSelfService                      | AuraDefinitionBundle | Existing lightning component used for <%=customerSafeName%> Self-Service Request page.                                  |
|                                                              |                      | This component has been modified to add action on different inputs in the form to notify the Case deflection component. |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>SupportSelfServiceProduct               | AuraDefinitionBundle | Existing lightning component used for <%=customerSafeName%> Self-Service Request step 1                                 |
|                                                              |                      | This component has been modified to add action on different inputs in the form to notify the Case deflection component. |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>SupportSelfServiceContact               | AuraDefinitionBundle | Existing lightning component used for <%=customerSafeName%> Self-Service Request step 2                                 |
|                                                              |                      | This component has been modified to add action on different inputs in the form to notify the Case deflection component. |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>Support_EmailToCaseFormDetail           | AuraDefinitionBundle | Existing lightning component used for <%=customerSafeName%> Email page                                                  |
|                                                              |                      | This component has been modified to add action on different inputs in the form to notify the Case deflection component. |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>Support_CallbackForm                    | AuraDefinitionBundle | Existing lightning component used for <%=customerSafeName%> Contact <%=customerSafeName%> page                          |
|                                                              |                      | This component has been modified to add action on different inputs in the form to notify the Case deflection component. |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>CommunityEmailCaseDeflection            | ApexComponent        | VF Component used to render suggested articles for the email/contact us case deflection                                 |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>CommunityFullSearch                     | ApexComponent        | VF Component required for community search page                                                                         |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>CommunityCaseDeflection                 | ApexComponent        | VF Component used to render suggested articles for the case deflection (not used anymore)                               |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>CommunitySelfServiceCaseDeflection      | ApexComponent        | VF Component used to render suggested articles for the Self-Service case deflection                                     |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>_bundle_assets                          | StaticResource       | Zip package that contains required custom coveo resources (css, js, fonts) for your implementation                      |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>CoveoSearchSetting__c                   | CustomObject         | Settings used to store different Coveo related information                                                              |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| CommunityFilterExpression__c                                 | CustomField          |                                                                                                                         |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>CoveoCultureFile                        | CustomLabel          | Used to dynamically inject proper culture file                                                                          |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>CommunityEmailCaseDeflectionTitle       | CustomLabel          | Title for Email/Contact <%=customerSafeName%> Case deflection                                                           |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+
| <%=customerSafeName%>CommunitySelfServiceCaseDeflectionTitle | CustomLabel          | Title for Self-Service <%=customerSafeName%> Case deflection                                                            |
+--------------------------------------------------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------+


**Code covering**

+-------------------------------------+-----------------------------------------+------------+
|            *Apex Class*             |            *Apex TEST Class*            | *Coverage* |
+=====================================+=========================================+============+
| VLC_Coveo_CommunitySearchController | VLC_Coveo_CommunitySearchControllerTest | 97%        |
+-------------------------------------+-----------------------------------------+------------+
| VLC_Coveo_EndpointHandlerController | VLC_Coveo_EndpointHandlerControllerTest | 100%       |
+-------------------------------------+-----------------------------------------+------------+

**Static resource**

.. code::

    <%=customerSafeName%>_bundle_assets
    └── js
        ├── cultures
        │   ├── en.js
        │   ├── es-es.js
        │   └── fr.js
        ├── <%=customerSafeName%>.bundle.js
        └── <%=customerSafeName%>.bundle.min.js


Custom Labels
-------------
If your change set includes custom labels, you can use the Salesforce Data Export tool or manually set the values.


Configuring Lightning components into your community
----------------------------------------------------

There is 3 pages into your community that need to be modified for the integration of the Coveo lightning custom components designed for your implementation.

    * Home Page
    * Search Page
    * Email Page

.. note:: No changes through the Community builder are required for ``Self-Service Request`` and ``Contact <%=customerSafeName%>`` Pages since the integration was made directly into the existing lightning components. 

**Home Page**

    1. In Salesforce, access the Community Builder.
        a. In Setup, search for and select All Communities.
        b. Next to your community, select Community Workspaces.
        c. In the new tab, under My Workspaces, select Builder.

    2. Select your Home page.
    3. Remove former Search box component.
    4. Drag & Drop the custom lightning component (``VLC_Coveo_CommunitySearchBox``) into your page.

    .. figure:: ../_static/img/SearchBoxDragDrop.png
        :align: center
        :alt: Coveo SearchBox drag and drop

    5. In the floating option box, enter the following information.

    .. figure:: ../_static/img/SearchBoxOptions.png
        :alt: Coveo SearchBox options

**Search Page**

    1. In Salesforce, access the Community Builder.
        a. In Setup, search for and select All Communities.
        b. Next to your community, select Community Workspaces.
        c. In the new tab, under My Workspaces, select Builder.
    2. Ensure you have created a page variation for your Search page (``Coveo Search``).

    .. figure:: ../_static/img/SearchPageVariation.png
        :align: center
        :alt: Coveo Search page variation

    .. note:: Make sure to target the desired audience and you have published your page.

    3. Select the new page variation.
    4. Drag & Drop the custom lightning component (``VLC_Coveo_CommunitySearch``) into your page.

    .. figure:: ../_static/img/SearchDragDrop.png
        :align: center
        :alt: Coveo Search page drag and drop

    5. In the floating option box, enter the following information.

    .. figure:: ../_static/img/SearchOptions.png
        :alt: Coveo Search page options
    

**Email Page**
    
    1. In Salesforce, access the Community Builder.
        a. In Setup, search for and select All Communities.
        b. Next to your community, select Community Workspaces.
        c. In the new tab, under My Workspaces, select Builder.
    2. Ensure you have created a page variation for Email page (``Email With Coveo``).

    .. figure:: ../_static/img/EmailPageVariation.png
        :align: center
        :alt: Email page variation

    .. note:: Make sure to target the desired audience and you have published your page.

    3. Select the new page variation
        a. Select page properties
        b. Under layout section, make sure to select 2 columns layout.

        .. figure:: ../_static/img/EmailLayout.png
            :alt: Open Case page layout
            :width: 50%

    4. Drag & Drop the custom lightning component (``VLC_Coveo_CommunityCaseDeflection``) into your page.

    .. figure:: ../_static/img/EmailDragDrop.png
        :align: center
        :alt: Open Case page drag and drop

    5. In the floating option box, enter the following information.

    .. figure:: ../_static/img/EmailOptions.png
        :alt: Open Case page options
        :width: 30%

.. warning:: If the ``VLC_Coveo_CommunityCaseDeflection`` throws an error saying the "Coveo Case Deflection" feature is not activated for your organization, this means the case deflection feature on the license has not been enabled. (This can be done by PS folks or Coveo Support)

.. important:: Don't forget to click on Publish to publish all recent changes to your community members :)

Post-Deployment Steps
=====================

Updating custom setting for the given Salesforce org
----------------------------------------------------


Smoke Tests
-----------

    * <%=customerSafeName%> Support community
        * Home page
        * Search page
        * Email page
        * Contact Us Page
        * Self-Service Requet Page


Clean-up
--------

    * Delete obsolete objects (e.g.: Apex classes, Apex Pages, etc).
