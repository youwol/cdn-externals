# YouWol's CDN externals

This repo gathers the bundles of external npm packages exposed in the YouWol's CDN.

This objective is to encapsulate them in ES modules, using a name versioned with respect to the version of the API.

Packages not properly exposed:
*  pyodide: a better way need to be used allowing for separation between pyodide and the pypi modules. 
Regarding the versioning, having multiple python interpreters in a project is not desirable.
*  mathjax: did not find a correct way to build the module. It won't work if multiple versions are loaded.
*  reflect-metadat: the package is used via the global variable Reflect -> multiple versions won't work.
