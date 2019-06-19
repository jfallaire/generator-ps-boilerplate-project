declare interface String {
  getInitials(glue?: boolean): string | Array<string>;
  capitalize(): string;
  camelize(): string;
  decamelize(separator): string;
}


String.prototype.getInitials = function (glue: boolean = true): string | Array<string> {

  var initials = this.replace(/[^a-zA-Z- ]/g, '').match(/\b\w/g) || [];

  if (glue) {
    return initials.join('');
  }

  return initials;
};

String.prototype.capitalize = function (): string {
  return this.toLowerCase().replace(/\b\w/g, function (m) {
    return m.toUpperCase();
  });
};

/**
* Camelize a string, cutting the string by multiple separators like
* hyphens, underscores and spaces.
* 
* @return string Camelized text
*/
String.prototype.camelize = function () {
  return this.replace(/^([A-Z])|[\s-_]+(\w)/g, function (match, p1, p2, offset) {
    if (p2) return p2.toUpperCase();
    return p1.toLowerCase();
  });
}

/**
 * Decamelizes a string with/without a custom separator (underscore by default).
 * 
 * @param str String in camelcase
 * @param separator Separator for the new decamelized string.
 */
String.prototype.decamelize = function (separator) {
  separator = typeof separator === 'undefined' ? '_' : separator;
  return this
    .replace(/([a-z\d])([A-Z])/g, '$1' + separator + '$2')
    .replace(/([A-Z]+)([A-Z][a-z\d]+)/g, '$1' + separator + '$2')
    .toLowerCase();
}
