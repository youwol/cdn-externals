import sys
from pathlib import Path

import requests

VERSION = sys.argv[1]

files = [
    'numpy.data',
    'numpy.js',
    'packages.json',
    'pandas.data',
    'pandas.js',
    'pyodide.asm.data',
    'pyodide.asm.js',
    'pyodide.asm.wasm',
    'pyodide.js',
    'python-dateutil.data',
    'python-dateutil.js',
    'pytz.data',
    'pytz.js',
    'six.data',
    'six.js',
    'distutils.js',
    'distutils.data',
    'setuptools.js',
    'setuptools.data',
    'pyparsing.js',
    'pyparsing.data',
    "pyodide_py.tar",
    "pyodide.js.map",
    'scikit-learn.js',
    'scikit-learn.data',
    'CLAPACK.js',
    'CLAPACK.data',
    'scipy.js',
    'scipy.data',
    'joblib.js',
    'joblib.data',
    'threadpoolctl.js',
    'threadpoolctl.data',
    ]

destination = Path('.') / VERSION / 'full'
if not destination.exists():
    destination.mkdir(parents=True)

for file in files:
    if(destination / file).exists():
        continue
    print(f"download {file}")
    url = f"https://cdn.jsdelivr.net/pyodide/v{VERSION}/full/{file}"
    r = requests.get(url, allow_redirects=True)
    print(f"save {file}")
    open(destination / file, 'wb').write(r.content)
