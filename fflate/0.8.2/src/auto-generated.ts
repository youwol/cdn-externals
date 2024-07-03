
const runTimeDependencies = {
    "externals": {},
    "includedInBundle": {
        "fflate": "0.8.2"
    }
}
const externals = {}
const exportedSymbols = {}

const entries = {
    'fflate': './index.ts',
}
export const setup = {
    name:'fflate',
    assetId:'ZmZsYXRl',
    version:'0.8.2',
    shortDescription:"High performance (de)compression in an 8kB package",
    apiVersion:'08',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

