
const runTimeDependencies = {
    "externals": {},
    "includedInBundle": {
        "pyodide": "0.25.0"
    }
}
const externals = {}
const exportedSymbols = {}

const entries = {
    'pyodide': './index.ts',
}
export const setup = {
    name:'pyodide',
    assetId:'cHlvZGlkZQ==',
    version:'0.25.0',
    shortDescription:"The Pyodide JavaScript package",
    apiVersion:'025',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

