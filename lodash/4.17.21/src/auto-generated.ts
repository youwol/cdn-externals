
const runTimeDependencies = {
    "externals": {},
    "includedInBundle": {
        "lodash": "4.17.21"
    }
}
const externals = {}
const exportedSymbols = {}

const entries = {
    'lodash': './index.ts',
}
export const setup = {
    name:'lodash',
    assetId:'bG9kYXNo',
    version:'4.17.21',
    shortDescription:"Lodash modular utilities.",
    apiVersion:'4',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

