declare var $A: { get: (key: string) => any };

const coveoCustomScripts = (promise, cmp) => {
  // Patch for known issue : https://coveord.atlassian.net/browse/SFINT-2137
  Coveo.SearchInterface.prototype['setupMobileFastclick'] = function() {};
  // Ensure String.locale match the current locale on community
  String['locale'] = $A.get("$Locale.language") || 'en';
  String['locale'] = String['locale'] == 'es' ? 'es-es' : String['locale'];
  // Ensure to set custom language dictionary properly for lightning community. 
  Coveo['setCustomLanguageDict']();
}

export function setCoveoCustomScripts() {

  window['coveoCustomScripts'] = {
    'default': coveoCustomScripts
  };
  
}