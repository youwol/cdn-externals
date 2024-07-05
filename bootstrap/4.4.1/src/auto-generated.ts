
const runTimeDependencies = {
    "externals": {
        "jquery": "^3.6.1",
        "popper.js": "^1.16.1"
    },
    "includedInBundle": {
        "bootstrap": "4.4.1"
    }
}
const externals = {
    "jquery": {
        "commonjs": "jquery",
        "commonjs2": "jquery",
        "root": "jquery_APIv3"
    },
    "popper.js": {
        "commonjs": "popper.js",
        "commonjs2": "popper.js",
        "root": "popper.js_APIv1"
    }
}
const exportedSymbols = {
    "jquery": {
        "apiKey": "3",
        "exportedSymbol": "jquery"
    },
    "popper.js": {
        "apiKey": "1",
        "exportedSymbol": "popper.js"
    }
}

const entries = {
    'bootstrap': './index.ts',
}
export const setup = {
    name:'bootstrap',
    assetId:'Ym9vdHN0cmFw',
    version:'4.4.1',
    shortDescription:"The most popular front-end framework for developing responsive, mobile first projects on the web.",
    apiVersion:'4',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

