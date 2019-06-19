
import { <%=capitalizeCustomerSafeName%>Helper } from '../../../src/typescripts/custo/<%=capitalizeCustomerSafeName%>Helper';

export function <%=capitalizeCustomerSafeName%>HelperTest() {
  describe('<%=capitalizeCustomerSafeName%>Helper', () => {
    it('should return empty string', ()=>{
      expect(<%=capitalizeCustomerSafeName%>Helper.yourHelperMethod).toEqual(jasmine.stringMatching(''));
    });
  });
}