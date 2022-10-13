# Pyodide CDN externals

This folder gather the publication of the pyodide environment as well as the packages bundled 
by the pyodide team.

The pyodide environment is defined in `./pyodide`, the packages bundled by the pyodide team are 
auto-generated using the script `create_packages.py` from the version of pyodide targeted.

After having executed the script the following actions are:
*  trigger the pipeline of pyodide
*  trigger the pipeline of all the packages (using the command below to add in `the yw_config.py` file)
*  copy the exportedSymbol in youwol_utils



