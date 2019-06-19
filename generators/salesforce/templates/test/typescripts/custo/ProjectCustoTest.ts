import * as Mock from '../../MockEnvironment';
import {
  IQueryResult,
  HighlightUtils,
  $$,
  QueryEvents
} from 'coveo-search-ui';

import { 
  <%=capitalizeCustomerSafeName%>Custo, 
  I<%=capitalizeCustomerSafeName%>Options } from '../../../src/typescripts/custo/<%=capitalizeCustomerSafeName%>Custo';
import { FakeResults } from '../../Fake';
import { Simulate } from '../../Simulate';


export function <%=capitalizeCustomerSafeName%>CustoTest() {
  describe('<%=capitalizeCustomerSafeName%>Custo', () => {
    let test: Mock.IBasicComponentSetup<<%=capitalizeCustomerSafeName%>Custo>;

    beforeEach(() => {
      test = Mock.basicComponentSetup<<%=capitalizeCustomerSafeName%>Custo>(<%=capitalizeCustomerSafeName%>Custo, undefined);
    });

    afterEach(() => {
      test = null;
    });

    it('is displaying nothing', () => {
      expect(test.cmp.element.innerHTML).toBe('');
    });

    it('should setup default pipeline context', () => {
      expect(test.cmp.getPipelineContext()).toEqual({});
    });

    describe('when pipeline context is specified', () => {
      const context = {
        qwerty: 'azerty',
        'a key': 'a value',
        'another key': ['multiple', 'values', 'in', 'array']
      };

      beforeEach(() => {
        test = Mock.optionsComponentSetup<<%=capitalizeCustomerSafeName%>Custo, I<%=capitalizeCustomerSafeName%>Options>(<%=capitalizeCustomerSafeName%>Custo, {
          pipelineContext: context
        });
      });

      afterEach(() => {
        test = null;
      });

      it('should add custom context in the query', () => {
        const simulation = Simulate.query(test.env);
        expect(simulation.queryBuilder.build().context).toEqual(
          jasmine.objectContaining({
            qwerty: 'azerty',
            'a key': 'a value',
            'another key': ['multiple', 'values', 'in', 'array']
          })
        );
      });
      it('should return the pipeline context', () => {
        expect(test.cmp.getPipelineContext()).toEqual(jasmine.objectContaining({
          qwerty: 'azerty',
          'a key': 'a value',
          'another key': ['multiple', 'values', 'in', 'array']
        }));
      });
      it('should support setting a new context', () => {
        test.cmp.setupPipelineContext({ abc: 'def', hij: ['klm', 'nop'] });
        expect(test.cmp.getPipelineContext()).toEqual(jasmine.objectContaining({ abc: 'def', hij: ['klm', 'nop'] }));
      });
    });

  });
}