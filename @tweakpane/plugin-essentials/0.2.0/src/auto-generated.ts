
const runTimeDependencies = {
    "externals": {
        "tweakpane": "^4.0.1"
    },
    "includedInBundle": {
        "@tweakpane/plugin-essentials": "0.2.0"
    }
}
const externals = {
    "tweakpane": {
        "commonjs": "tweakpane",
        "commonjs2": "tweakpane",
        "root": "tweakpane_APIv4"
    }
}
const exportedSymbols = {
    "tweakpane": {
        "apiKey": "4",
        "exportedSymbol": "tweakpane"
    }
}

const entries = {
    '@tweakpane/plugin-essentials': './index.ts',
}
export const setup = {
    name:'@tweakpane/plugin-essentials',
    assetId:'QHR3ZWFrcGFuZS9wbHVnaW4tZXNzZW50aWFscw==',
    version:'0.2.0',
    shortDescription:"Essential components for Tweakpane",
    apiVersion:'02',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

