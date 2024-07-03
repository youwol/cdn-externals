
const runTimeDependencies = {
    "externals": {
        "fflate": "^0.8.2",
        "potpack": "^2.0.0",
        "draco3d": "^1.5.7",
        "three": "^0.152.0"
    },
    "includedInBundle": {
        "three-stdlib": "2.30.3"
    }
}
const externals = {
    "fflate": {
        "commonjs": "fflate",
        "commonjs2": "fflate",
        "root": "fflate_APIv08"
    },
    "potpack": {
        "commonjs": "potpack",
        "commonjs2": "potpack",
        "root": "potpack_APIv2"
    },
    "draco3d": {
        "commonjs": "draco3d",
        "commonjs2": "draco3d",
        "root": "draco3d_APIv1"
    },
    "three": {
        "commonjs": "three",
        "commonjs2": "three",
        "root": "THREE_APIv0152"
    }
}
const exportedSymbols = {
    "fflate": {
        "apiKey": "08",
        "exportedSymbol": "fflate"
    },
    "potpack": {
        "apiKey": "2",
        "exportedSymbol": "potpack"
    },
    "draco3d": {
        "apiKey": "1",
        "exportedSymbol": "draco3d"
    },
    "three": {
        "apiKey": "0152",
        "exportedSymbol": "THREE"
    }
}

const entries = {
    'three-stdlib': './index.ts',
}
export const setup = {
    name:'three-stdlib',
    assetId:'dGhyZWUtc3RkbGli',
    version:'2.30.3',
    shortDescription:"stand-alone library of threejs examples",
    apiVersion:'2',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

