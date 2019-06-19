
import { IMockEnvironment } from './MockEnvironment';
import { FakeResults } from './Fake';
import _ = require('underscore');
import {
  $$,
  IQuery,
  QueryEvents,
  QueryBuilder,
  IQueryResults,
  IEndpointError,
  IQueryCorrection,
  IGroupByResult,
  INewQueryEventArgs,
  IBuildingQueryEventArgs,
  IDuringQueryEventArgs,
  IQueryErrorEventArgs,
  IPreprocessResultsEventArgs,
  INoResultsEventArgs,
  IQuerySuccessEventArgs,
  NoopComponent,
  Component,
  QueryError,
  InitializationEvents,
  Defer,
  Utils,
  IOmniboxData,OmniboxEvents,
  IBreadcrumbItem, IPopulateBreadcrumbEventArgs, BreadcrumbEvents
} from 'coveo-search-ui';
import ModalBox = Coveo.ModalBox.ModalBox;

export interface ISimulateQueryData {
  query?: IQuery;
  queryBuilder?: QueryBuilder;
  searchAsYouType?: boolean;
  promise?: Promise<IQueryResults>;
  error?: IEndpointError;
  results?: IQueryResults;
  queryCorrections?: IQueryCorrection[];
  groupByResults?: IGroupByResult[];
  callbackDuringQuery?: () => void;
  callbackAfterNoResults?: () => void;
  callbackAfterQuery?: () => void;
  doNotFlushDefer?: boolean;
  deferSuccess?: boolean;
  cancel?: boolean;
  origin?: Component;
}

export class Simulate {
  static isPhantomJs() {
    return navigator.userAgent.indexOf('PhantomJS') != -1;
  }

  static isChromeHeadless() {
    return navigator.userAgent.indexOf('HeadlessChrome') != -1;
  }

  static queryError(env: IMockEnvironment, options?: ISimulateQueryData): ISimulateQueryData {
    options = _.extend(
      {},
      {
        error: new QueryError({
          statusCode: 500,
          data: {
            message: 'oh',
            type: 'no!'
          }
        })
      },
      options
    );
    return Simulate.query(env, options);
  }

  static query(env: IMockEnvironment, options?: ISimulateQueryData): ISimulateQueryData {
    options = _.extend(
      {},
      {
        query: new QueryBuilder().build(),
        queryBuilder: new QueryBuilder(),
        searchAsYouType: false,
        promise: new Promise(() => {}),
        results: FakeResults.createFakeResults(),
        callbackDuringQuery: () => {},
        callbackAfterNoResults: () => {},
        callbackAfterQuery: () => {},
        deferSuccess: false,
        cancel: false,
        origin: NoopComponent
      },
      options
    );

    if (options.queryCorrections) {
      options.results.queryCorrections = options.queryCorrections;
    }
    if (options.groupByResults) {
      options.results.groupByResults = options.groupByResults;
    }

    var newQueryEventArgs: INewQueryEventArgs = {
      searchAsYouType: options.searchAsYouType,
      cancel: options.cancel,
      origin: options.origin,
      shouldRedirectStandaloneSearchbox: true
    };
    $$(env.root).trigger(QueryEvents.newQuery, newQueryEventArgs);

    var buildingQueryEventArgs: IBuildingQueryEventArgs = {
      queryBuilder: options.queryBuilder,
      searchAsYouType: false,
      cancel: false
    };
    $$(env.root).trigger(QueryEvents.buildingQuery, buildingQueryEventArgs);
    $$(env.root).trigger(QueryEvents.doneBuildingQuery, buildingQueryEventArgs);

    if (newQueryEventArgs.cancel || buildingQueryEventArgs.cancel) {
      return options;
    }

    var duringQueryEventArgs: IDuringQueryEventArgs = {
      query: options.query,
      queryBuilder: options.queryBuilder,
      promise: options.promise,
      searchAsYouType: options.searchAsYouType
    };
    $$(env.root).trigger(QueryEvents.duringQuery, duringQueryEventArgs);
    options.callbackDuringQuery();

    var success = () => {
      if (Utils.exists(options.error)) {
        var queryErrorEventArgs: IQueryErrorEventArgs = {
          queryBuilder: options.queryBuilder,
          query: options.query,
          endpoint: env.searchEndpoint,
          error: options.error,
          searchAsYouType: options.searchAsYouType
        };
        Promise.reject(options.promise).catch(e => {});
        $$(env.root).trigger(QueryEvents.queryError, queryErrorEventArgs);
      } else {
        var preprocessResultsEventArgs: IPreprocessResultsEventArgs = {
          queryBuilder: options.queryBuilder,
          query: options.query,
          results: options.results,
          searchAsYouType: options.searchAsYouType
        };
        $$(env.root).trigger(QueryEvents.preprocessResults, preprocessResultsEventArgs);

        var noResultsEventArgs: INoResultsEventArgs = {
          query: options.query,
          queryBuilder: options.queryBuilder,
          results: options.results,
          searchAsYouType: options.searchAsYouType,
          retryTheQuery: false
        };

        if (options.results.totalCount == 0 || options.results.results.length == 0) {
          $$(env.root).trigger(QueryEvents.noResults, noResultsEventArgs);
          options.callbackAfterNoResults();
        }

        if (noResultsEventArgs.retryTheQuery) {
          // do nothing, as this could cause test to loop endlessly if they do not handle the query being retried.
        } else {
          var querySuccessEventArgs: IQuerySuccessEventArgs = {
            query: options.query,
            queryBuilder: options.queryBuilder,
            results: options.results,
            searchAsYouType: options.searchAsYouType
          };
          $$(env.root).trigger(QueryEvents.querySuccess, querySuccessEventArgs);
          $$(env.root).trigger(QueryEvents.deferredQuerySuccess, querySuccessEventArgs);
        }
      }

      if (!options.doNotFlushDefer) {
        Defer.flush();
      }

      options.callbackAfterQuery();
    };

    if (options.deferSuccess) {
      Defer.defer(success);
    } else {
      success();
    }

    return options;
  }

  static initialization(env: IMockEnvironment) {
    $$(env.root).trigger(InitializationEvents.beforeInitialization);
    $$(env.root).trigger(InitializationEvents.afterComponentsInitialization);
    $$(env.root).trigger(InitializationEvents.restoreHistoryState);
    $$(env.root).trigger(InitializationEvents.afterInitialization);
  }

  static modalBoxModule(): ModalBox {
    let modalBox = <any>{};
    modalBox.open = jasmine.createSpy('open');
    modalBox.close = jasmine.createSpy('close');
    modalBox.open.and.returnValue({
      modalBox: $$('div', undefined, $$('div', { className: 'coveo-wrapper' })).el,
      wrapper: $$('div', undefined, $$('div', { className: 'coveo-quickview-close-button' })).el,
      overlay: $$('div').el,
      content: $$('div').el,
      close: modalBox.close
    });
    return modalBox;
  }

  static analyticsStoreModule(actionsHistory = []) {
    return {
      addElement: (query: IQuery) => {},
      getHistory: () => {
        return actionsHistory;
      },
      setHistory: (history: any[]) => {},
      clear: () => {},
      getMostRecentElement: () => {
        return null;
      }
    };
  }

  static populateOmnibox(env: IMockEnvironment, options?): IOmniboxData {
    let expression = {
      word: 'foo',
      regex: /foo/
    };

    var fakeOmniboxArgs = _.extend(
      {},
      {
        rows: [],
        completeQueryExpression: expression,
        allQueryExpression: expression,
        currentQueryExpression: expression,
        cursorPosition: 3,
        clear: jasmine.createSpy('clear'),
        clearCurrentExpression: jasmine.createSpy('clearCurrent'),
        replace: jasmine.createSpy('replace'),
        replaceCurrentExpression: jasmine.createSpy('replaceCurrentExpression'),
        insertAt: jasmine.createSpy('insertAt'),
        closeOmnibox: jasmine.createSpy('closeOmnibox')
      },
      options
    );

    $$(env.root).trigger(OmniboxEvents.populateOmnibox, fakeOmniboxArgs);

    return fakeOmniboxArgs;
  }

  static breadcrumb(env: IMockEnvironment, options?): IBreadcrumbItem[] {
    let args = <IPopulateBreadcrumbEventArgs>{ breadcrumbs: [] };
    $$(env.root).trigger(BreadcrumbEvents.populateBreadcrumb, args);
    return args.breadcrumbs;
  }

  static clearBreadcrumb(env: IMockEnvironment) {
    $$(env.root).trigger(BreadcrumbEvents.clearBreadcrumb);
  }

  static keyUp(element: HTMLElement, key: number, shiftKey?: boolean) {
    return Simulate.keyEvent(element, key, 'keyup', shiftKey);
  }

  static keyDown(element: HTMLElement, key: number, shiftKey?: boolean) {
    return Simulate.keyEvent(element, key, 'keydown', shiftKey);
  }

  static keyEvent(element: HTMLElement, key: number, eventName: string, shiftKey?: boolean) {
    const event = new KeyboardEvent(eventName, { shiftKey: shiftKey });
    Object.defineProperty(event, 'keyCode', {
      get: () => {
        return key;
      }
    });
    Object.defineProperty(event, 'which', {
      get: () => {
        return key;
      }
    });
    element.dispatchEvent(event);
    Defer.flush();
  }
}