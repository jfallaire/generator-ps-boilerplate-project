// All modules are imported to be included in the code coverage report.
import '../src/typescripts/Index.ts';

import { SalesforceCommunityResultLinkTest } from './typescripts/ui/SalesforceCommunityResultLinkTest';
SalesforceCommunityResultLinkTest();

import { <%=capitalizeCustomerSafeName%>CustoTest } from './typescripts/custo/<%=capitalizeCustomerSafeName%>CustoTest';
<%=capitalizeCustomerSafeName%>CustoTest();

import { <%=capitalizeCustomerSafeName%>HelperTest } from './typescripts/custo/<%=capitalizeCustomerSafeName%>HelperTest';
<%=capitalizeCustomerSafeName%>HelperTest();


