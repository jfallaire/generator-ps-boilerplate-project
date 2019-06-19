

export * from './<%= capitalizeCustomerSafeName %>Core';
// your custo component
export * from './custo/<%= capitalizeCustomerSafeName %>Custo';

// your ui components here
export { SalesforceCommunityResultLink } from './ui/SalesforceCommunityResultLink/SalesforceCommunityResultLink';

import { swapVar } from './SwapVar';
swapVar(this);

import { setCoveoCustomScripts } from './CoveoCustomScripts';
setCoveoCustomScripts();

// your culture files here (for webpack)
import './cultures/en.js'
import './cultures/fr.js'
import './cultures/es-es.js'
