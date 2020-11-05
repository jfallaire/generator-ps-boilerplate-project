

export * from './<%= capitalizeCustomerSafeName %>Core';
// your custo component
export * from './custo/<%= capitalizeCustomerSafeName %>Custo';

// your ui components here

import { swapVar } from '@coveops/turbo-core';
swapVar(this)


// cultures for webpack
import './cultures/en.js'
import './cultures/fr.js'
import './cultures/es-es.js'
