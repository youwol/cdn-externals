
const runTimeDependencies = {
    "externals": {
        "bootstrap": "^4.0.0",
        "jquery": "^3.6.1"
    },
    "includedInBundle": {
        "bootstrap-select": "1.13.18"
    }
}
const externals = {
    "bootstrap": {
        "commonjs": "bootstrap",
        "commonjs2": "bootstrap",
        "root": "bootstrap_APIv4"
    },
    "jquery": {
        "commonjs": "jquery",
        "commonjs2": "jquery",
        "root": ["jquery_APIv3", "default"]
    }
}
const exportedSymbols = {
    "bootstrap": {
        "apiKey": "4",
        "exportedSymbol": "bootstrap"
    },
    "jquery": {
        "apiKey": "3",
        "exportedSymbol": "jquery"
    }
}

const entries = {
    'bootstrap-select': './index.ts',
}
export const setup = {
    name:'bootstrap-select',
    assetId:'Ym9vdHN0cmFwLXNlbGVjdA==',
    version:'1.13.18',
    shortDescription:"The jQuery plugin that brings select elements into the 21st century with intuitive multiselection, searching, and much more. Now with Bootstrap 4 support.",
    apiVersion:'1',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

