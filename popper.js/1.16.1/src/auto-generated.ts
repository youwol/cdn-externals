
const runTimeDependencies = {
    "externals": {},
    "includedInBundle": {
        "popper.js": "1.16.1"
    }
}
const externals = {}
const exportedSymbols = {}

const entries = {
    'popper.js': './index.ts',
}
export const setup = {
    name:'popper.js',
    assetId:'cG9wcGVyLmpz',
    version:'1.16.1',
    shortDescription:"A kickass library to manage your poppers",
    apiVersion:'1',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

