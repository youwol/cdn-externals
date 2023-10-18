
const runTimeDependencies = {
    "externals": {},
    "includedInBundle": {
        "tweakpane": "4.0.1"
    }
}
const externals = {}
const exportedSymbols = {}

const entries = {
    'tweakpane': './index.ts',
}
export const setup = {
    name:'tweakpane',
    assetId:'dHdlYWtwYW5l',
    version:'4.0.1',
    shortDescription:"A compact pane for fine-tuning parameters and monitoring value changes",
    apiVersion:'4',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

