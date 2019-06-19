import * as Mock from '../../MockEnvironment';
import {
  IQueryResult,
  HighlightUtils,
  ResultLink,
  $$
} from 'coveo-search-ui';

import { 
  SalesforceCommunityResultLink, 
  ISalesforceCommunityResultLinkOptions } from '../../../src/typescripts/ui/SalesforceCommunityResultLink/SalesforceCommunityResultLink';
import { FakeResults } from '../../Fake';

export function SalesforceCommunityResultLinkTest() {

  describe('SalesforceCommunityResultLink', () => {
    let test: Mock.IBasicComponentSetup<SalesforceCommunityResultLink>;
    let fakeResult: IQueryResult;

    beforeEach(() => {
      fakeResult = initFakeResult();
      test = Mock.advancedResultComponentSetup<SalesforceCommunityResultLink>(SalesforceCommunityResultLink, fakeResult, undefined);
      let resultLinkCmp = <ResultLink>Coveo.get(test.cmp.element, ResultLink.ID);
      spyOn(resultLinkCmp, 'openLink');
      spyOn(window, 'open');
    });

    afterEach(function() {
      test = null;
      fakeResult = null;
    });

    it('should have its tabindex value set to 0', () => {
      expect(test.cmp.element.getAttribute('tabindex')).toBe('0');
    });

    it('should highlight the result title', () => {
      expect(test.cmp.element.innerHTML).toEqual(
        HighlightUtils.highlightString(fakeResult.title, fakeResult.titleHighlights, null, 'coveo-highlight')
      );
    });

    it('should contain the clickUri if the result has no title', () => {
      fakeResult.title = undefined;
      test = Mock.advancedResultComponentSetup<SalesforceCommunityResultLink>(SalesforceCommunityResultLink, fakeResult, undefined);
      expect(test.cmp.element.innerHTML).toEqual(fakeResult.clickUri);
    });

    it('can receive an onClick option to execute', done => {
      test = Mock.advancedResultComponentSetup<SalesforceCommunityResultLink>(
        SalesforceCommunityResultLink,
        fakeResult,
        new Mock.AdvancedComponentSetupOptions($$('div').el, {
          onClick: () => {
            expect(true).toBe(true);
            done();
          }
        })
      );
      $$(test.cmp.element).trigger('click');
    });

    it('sends an analytic event on click', () => {
      $$(test.cmp.element).trigger('click');
      expect(test.cmp.usageAnalytics.logClickEvent).toHaveBeenCalledTimes(1);
    });

    it('sends an analytics event on context menu', () => {
      $$(test.cmp.element).trigger('contextmenu');
      expect(test.cmp.usageAnalytics.logClickEvent).toHaveBeenCalledTimes(1);
    });

    it('sends an analytics event on mouseup', () => {
      $$(test.cmp.element).trigger('mouseup');
      expect(test.cmp.usageAnalytics.logClickEvent).toHaveBeenCalledTimes(1);
    });

    it('sends an analytics event on mousedown', () => {
      $$(test.cmp.element).trigger('mousedown');
      expect(test.cmp.usageAnalytics.logClickEvent).toHaveBeenCalledTimes(1);
    });

    it('does not send multiple analytics events with multiple mouse events', () => {
      $$(test.cmp.element).trigger('mousedown');
      $$(test.cmp.element).trigger('click');
      $$(test.cmp.element).trigger('mouseup');
      expect(test.cmp.usageAnalytics.logClickEvent).toHaveBeenCalledTimes(1);
    });

    it('sends an event 1s after a long press on mobile', done => {
      $$(test.cmp.element).trigger('touchstart');
      expect(test.cmp.usageAnalytics.logClickEvent).not.toHaveBeenCalled();
      setTimeout(() => {
        expect(test.cmp.usageAnalytics.logClickEvent).toHaveBeenCalledTimes(1);
        done();
      }, 1100);
    });

    it('does not send an event if a touchend event occurs before a 1s delay', done => {
      $$(test.cmp.element).trigger('touchstart');

      setTimeout(() => {
        $$(test.cmp.element).trigger('touchend');
      }, 300);

      setTimeout(() => {
        expect(test.cmp.usageAnalytics.logClickEvent).not.toHaveBeenCalled();
        done();
      }, 1100);
    });

    describe('exposes hrefTemplate', () => {
      it('should not modify the href template if there are no field specified', () => {
        let hrefTemplate = 'test';
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, { hrefTemplate: hrefTemplate }, fakeResult);
        test.cmp.resultLinkCmp.openLinkInNewWindow();
        expect(window.open).toHaveBeenCalledWith(hrefTemplate, jasmine.anything());
      });

      it('should replace fields in the href template by the results equivalent', () => {
        let hrefTemplate = '${title}';
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, { hrefTemplate: hrefTemplate }, fakeResult);
        test.cmp.resultLinkCmp.openLinkInNewWindow();
        expect(window.open).toHaveBeenCalledWith(fakeResult.title, jasmine.anything());
      });

      it('should support nested values in result', () => {
        let hrefTemplate = '${raw.number}';
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, { hrefTemplate: hrefTemplate }, fakeResult);
        test.cmp.resultLinkCmp.openLinkInNewWindow();
        expect(window.open).toHaveBeenCalledWith(fakeResult.raw['number'].toString(), jasmine.anything());
      });

      it('should not parse standalone accolades', () => {
        let hrefTemplate = '${raw.number}{test}';
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, { hrefTemplate: hrefTemplate }, fakeResult);
        test.cmp.resultLinkCmp.openLinkInNewWindow();
        expect(window.open).toHaveBeenCalledWith(fakeResult.raw['number'] + '{test}', jasmine.anything());
      });

      it('should support external fields', () => {
        window['Coveo']['test'] = 'testExternal';
        let hrefTemplate = '${Coveo.test}';
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, { hrefTemplate: hrefTemplate }, fakeResult);
        test.cmp.resultLinkCmp.openLinkInNewWindow();
        expect(window.open).toHaveBeenCalledWith('testExternal', jasmine.anything());
        window['Coveo']['test'] = undefined;
      });

      it('should support nested external fields with more than 2 keys', () => {
        window['Coveo']['test'] = { key: 'testExternal' };
        let hrefTemplate = '${Coveo.test.key}';
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, { hrefTemplate: hrefTemplate }, fakeResult);
        test.cmp.resultLinkCmp.openLinkInNewWindow();
        expect(window.open).toHaveBeenCalledWith('testExternal', jasmine.anything());
        window['Coveo']['test'] = undefined;
      });
    });

    describe('when the element is a hyperlink', () => {
      beforeEach(() => {
        test = Mock.advancedResultComponentSetup<SalesforceCommunityResultLink>(SalesforceCommunityResultLink, fakeResult, new Mock.AdvancedComponentSetupOptions($$('a').el));
      });

      it('should set the href to the result click uri', () => {
        expect(test.cmp.element.getAttribute('href')).toEqual(fakeResult.clickUri);
      });

      it('should not override the href if it is set before the initialization', () => {
        let element = $$('a');
        let href = 'javascript:void(0)';
        element.setAttribute('href', href);
        test = Mock.advancedResultComponentSetup<SalesforceCommunityResultLink>(SalesforceCommunityResultLink, fakeResult, new Mock.AdvancedComponentSetupOptions(element.el));

        expect(test.cmp.element.getAttribute('href')).toEqual(href);
      });

    });

    describe('when enabling url rewriter option', () => {
      let options: ISalesforceCommunityResultLinkOptions = {};
      beforeEach(() => {
        options = { enableUrlRewriter: true };
        fakeResult.raw.sfcaseid = 'test';
        fakeResult.raw.sfid = 'test';
        fakeResult.raw.sfcontentdocumentid = 'test';
        fakeResult.raw.sfideaid = 'test';
        fakeResult.raw.sfurlname = 'test';
        fakeResult.raw.sfid = 'test';
        fakeResult.raw.sflanguage = 'test';
      });

      it('should modify the clickUri if objecttype is Case', ()=> {
        fakeResult.raw.objecttype = 'Case';
        fakeResult.raw.sfcaseid = 'test';
        const oldClickUri = fakeResult.clickUri;
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, options, fakeResult);
        expect(oldClickUri).not.toEqual(fakeResult.clickUri);
        expect(fakeResult.clickUri).toContain('/s/case');
      });

      it('should modify the clickUri if objecttype is CollaborationGroup', ()=>{
        fakeResult.raw.objecttype = 'CollaborationGroup';
        const oldClickUri = fakeResult.clickUri;
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, options, fakeResult);
        expect(oldClickUri).not.toEqual(fakeResult.clickUri);
        expect(fakeResult.clickUri).toContain('/s/group');
      });

      it('should modify the clickUri if objecttype is ContentVersion', ()=>{
        fakeResult.raw.objecttype = 'ContentVersion';
        const oldClickUri = fakeResult.clickUri;
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, options, fakeResult);
        expect(oldClickUri).not.toEqual(fakeResult.clickUri);
        expect(fakeResult.clickUri).toContain('/s/contentdocument');
      });

      it('should modify the clickUri if objecttype is Idea', ()=>{
        fakeResult.raw.objecttype = 'Idea';
        const oldClickUri = fakeResult.clickUri;
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, options, fakeResult);
        expect(oldClickUri).not.toEqual(fakeResult.clickUri);
        expect(fakeResult.clickUri).toContain('/s/idea');
      });

      it('should modify the clickUri if result is Knowledge Base', ()=>{
        fakeResult.raw.sfkbid = 'test';
        const oldClickUri = fakeResult.clickUri;
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, options, fakeResult);
        expect(oldClickUri).not.toEqual(fakeResult.clickUri);
        expect(fakeResult.clickUri).toContain('/s/article');
      });

      it('should add query string parameter language when enabling language option', ()=>{
        fakeResult.raw.sfkbid = 'test';
        options.enableLanguage = true;
        const oldClickUri = fakeResult.clickUri;
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, options, fakeResult);
        expect(oldClickUri).not.toEqual(fakeResult.clickUri);
        expect(fakeResult.clickUri).toContain('?language=');
      });

      it('should not add query string parameter language when no language option', ()=>{
        fakeResult.raw.sfkbid = 'test';
        options.enableLanguage = false;
        const oldClickUri = fakeResult.clickUri;
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, options, fakeResult);
        expect(oldClickUri).not.toEqual(fakeResult.clickUri);
        expect(fakeResult.clickUri).not.toContain('?language=');
      });

      describe('when the objecttype is either FeedItem or FeedComment', () => {
        beforeEach(() => {
          fakeResult.raw.objecttype = 'FeedItem';
          fakeResult.raw.sffeeditemid = 'test';
        });

        it('should modify the clickUri if there is no sfparentid', ()=>{
          const oldClickUri = fakeResult.clickUri;
          test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, options, fakeResult);
          expect(oldClickUri).not.toEqual(fakeResult.clickUri);
          expect(fakeResult.clickUri).toContain('/s/feed');
        })
        it('should modify the clickUri if parent item is a question', ()=>{
          fakeResult.raw.sfparentid = '005test';
          const oldClickUri = fakeResult.clickUri;
          test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, options, fakeResult);
          expect(oldClickUri).not.toEqual(fakeResult.clickUri);
          expect(fakeResult.clickUri).toContain('/s/question');
        })
      });

      it('should not modify the clickUri if no matching condition', ()=>{
        fakeResult.raw = {};
        const oldClickUri = fakeResult.clickUri;
        test = Mock.optionsResultComponentSetup<SalesforceCommunityResultLink, ISalesforceCommunityResultLinkOptions>(SalesforceCommunityResultLink, options, fakeResult);
        expect(oldClickUri).toEqual(fakeResult.clickUri);
      });
    });
  });

  function initFakeResult(): IQueryResult {
    let fakeResult = FakeResults.createFakeResult();
    fakeResult.title = 'A test title';
    fakeResult.titleHighlights = [{ offset: 2, length: 4 }];
    fakeResult.clickUri = 'uri';
    return fakeResult;
  }
}