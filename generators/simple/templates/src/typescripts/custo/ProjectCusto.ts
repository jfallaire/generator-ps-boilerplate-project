import $$ = Coveo.$$;
import Component = Coveo.Component;
import Initialization = Coveo.Initialization;
import ComponentOptions = Coveo.ComponentOptions;
import IComponentBindings = Coveo.IComponentBindings;
import IBuildingQueryEventArgs = Coveo.IBuildingQueryEventArgs;
import IDoneBuildingQueryEventArgs = Coveo.IDoneBuildingQueryEventArgs;
import IPreprocessResultsEventArgs = Coveo.IPreprocessResultsEventArgs;
import INewQueryEventArgs = Coveo.INewQueryEventArgs;
import IAttributeChangedEventArg = Coveo.IAttributeChangedEventArg;
import { <%= capitalizeCustomerSafeName %>Helper } from './<%= capitalizeCustomerSafeName %>Helper';
import IStringMap = Coveo.IStringMap;

declare var String: { toLocaleString: (param: any) => void; };

export interface I<%= capitalizeCustomerSafeName %>Options {
  pipelineContext: IStringMap<any>
}

/**
 * Required customization specifically applied for your implementation
 */
export class <%= capitalizeCustomerSafeName %>Custo extends Component {

  static ID = '<%= capitalizeCustomerSafeName %>Custo';

  private context: IStringMap<any>;

  static options: I<%= capitalizeCustomerSafeName %>Options = {
    pipelineContext: Coveo.ComponentOptions.buildJsonOption()
  };

  constructor(public element: HTMLElement, public options: I<%= capitalizeCustomerSafeName %>Options, public bindings?: IComponentBindings) {

    super(element, <%= capitalizeCustomerSafeName %>Custo.ID, bindings);
    this.options = ComponentOptions.initComponentOptions(element, <%= capitalizeCustomerSafeName %>Custo, options);

    this.setupPipelineContext(this.options.pipelineContext);

    this.bind.onRootElement(Coveo.QueryEvents.buildingQuery, this.handleBuildingQuery);

  }

  public setupPipelineContext(data: IStringMap<any>) {
    this.context = _.pick(data, _.identity) || {};
  }

  public getPipelineContext() {
    return this.context;
  }

  private handleBuildingQuery(data: Coveo.IBuildingQueryEventArgs) {
    data.queryBuilder.addContext(this.context);
  }

};

Initialization.registerAutoCreateComponent(<%= capitalizeCustomerSafeName %>Custo);

