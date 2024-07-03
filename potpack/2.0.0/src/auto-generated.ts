
const runTimeDependencies = {
    "externals": {},
    "includedInBundle": {
        "potpack": "2.0.0"
    }
}
const externals = {}
const exportedSymbols = {}

const entries = {
    'potpack': './index.ts',
}
export const setup = {
    name:'potpack',
    assetId:'cG90cGFjaw==',
    version:'2.0.0',
    shortDescription:"A tiny library for packing 2D rectangles (for sprite layouts)",
    apiVersion:'2',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

