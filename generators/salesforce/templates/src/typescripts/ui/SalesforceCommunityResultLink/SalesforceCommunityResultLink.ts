import Component = Coveo.Component;
import Initialization = Coveo.Initialization;
import ComponentOptions = Coveo.ComponentOptions;
import IComponentBindings = Coveo.IComponentBindings;
import IQueryResult = Coveo.IQueryResult;
import IResultsComponentBindings = Coveo.IResultsComponentBindings;

export interface ISalesforceCommunityResultLinkOptions extends Coveo.IResultLinkOptions {
    useAsPrintable?: boolean;
    enableUrlRewriter?: boolean;
    enableLanguage?: boolean;
    name?: string;
    hostName?: string;
    protocol?: string;
}

const fields = [
    '@sfcaseid',
    '@objecttype',
    '@sfparentid',
    '@sffeeditemid',
    '@sfid',
    '@sfcontentdocumentid',
    '@sfideaid',
    '@sfkbid',
    '@sfurlname',
    '@sflanguage'
];

export class SalesforceCommunityResultLink extends Component {
    static ID = 'SalesforceCommunityResultLink';

    public resultLinkCmp: Coveo.ResultLink;

    /**
     * The options for the component
     * @componentOptions
     */
    static options: ISalesforceCommunityResultLinkOptions = {
        enableUrlRewriter: Coveo.ComponentOptions.buildBooleanOption({ defaultValue: true }),
        enableLanguage: Coveo.ComponentOptions.buildBooleanOption({ defaultValue: false }),
        useAsPrintable: Coveo.ComponentOptions.buildBooleanOption({ defaultValue: false }),
        name: Coveo.ComponentOptions.buildStringOption({ defaultValue: '' }),
        hostName: Coveo.ComponentOptions.buildStringOption({ defaultValue: window.location.hostname }),
        protocol: Coveo.ComponentOptions.buildStringOption({ defaultValue: window.location.protocol })
    };

    constructor(
        public element: HTMLElement,
        public options: ISalesforceCommunityResultLinkOptions,
        bindings?: IResultsComponentBindings,
        public result?: IQueryResult
    ) {

        super(element, SalesforceCommunityResultLink.ID, bindings);

        this.options = ComponentOptions.initComponentOptions(element, SalesforceCommunityResultLink, options);
        this.result = result;
        

        if (this.options.enableUrlRewriter) {
            this.applyCommunityUrlRewriter();
        }

        if (this.options.useAsPrintable) {
            this.element.textContent = this.result.clickUri;
        }

        this.resultLinkCmp = new Coveo.ResultLink(this.element, this.options, bindings, result);
    }

    private applyCommunityUrlRewriter() {

        const communityUrl = SalesforceCommunityResultLink.getCommunityUrl(this.result, this.options);
        if (communityUrl) {
            this.result.clickUri = this.result['ClickUri'] = this.result.raw.clickableuri = this.result.raw.sysclickableuri = communityUrl;
        }
    }

    public static getCommunityName(options:ISalesforceCommunityResultLinkOptions) {
        let communityName = window.location.pathname.replace(/\/(.*)\/s\/(.*)/i, '$1');
        communityName = options.name || (communityName != window.location.pathname ? communityName : '');

        return communityName;
    }

    public static getCommunityUrl(result: Coveo.IQueryResult, options:ISalesforceCommunityResultLinkOptions) {
        const communityName = SalesforceCommunityResultLink.getCommunityName(options);
        const communityPath = communityName ? `/${communityName}` : '';
        const communityBaseUrl = `${options.protocol}//${options.hostName}${communityPath}`;
        let communityUrl = '';

        if (result.raw.objecttype == 'Case') {
            communityUrl = `${communityBaseUrl}/s/case/${result.raw.sfcaseid}`;
        } else if (result.raw.objecttype == 'FeedItem' || result.raw.objecttype == 'FeedComment') {
            const parentId:string = result.raw.sfparentid || '';
            const path = parentId.substr(0,3) == '005' ? 'question' : 'feed';
            communityUrl = `${communityBaseUrl}/s/${path}/${result.raw.sffeeditemid || result.raw.sfid}`;
        } else if (result.raw.objecttype == 'CollaborationGroup') {
            communityUrl = `${communityBaseUrl}/s/group/${result.raw.sfid}`;
        } else if (result.raw.objecttype == 'ContentVersion') {
            communityUrl = `${communityBaseUrl}/s/contentdocument/${result.raw.sfcontentdocumentid}`;
        } else if (result.raw.objecttype == 'Idea') {
            communityUrl = `${communityBaseUrl}/s/idea/${(result.raw.sfideaid || result.raw.sfid)}/detail`;
        } else if (result.raw.sfkbid) {
            communityUrl = `${communityBaseUrl}/s/article/${result.raw.sfurlname}`;
        }
        
        communityUrl = communityUrl && options.enableLanguage ? `${communityUrl}?language=${ result.raw.sflanguage || 'en_US' }`: communityUrl;


        return communityUrl;
    }
}

Initialization.registerAutoCreateComponent(SalesforceCommunityResultLink);
Initialization.registerComponentFields(SalesforceCommunityResultLink.ID, fields); 

