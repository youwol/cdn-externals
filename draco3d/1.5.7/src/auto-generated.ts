
const runTimeDependencies = {
    "externals": {},
    "includedInBundle": {
        "draco3d": "1.5.7"
    }
}
const externals = {}
const exportedSymbols = {}

const entries = {
    'draco3d': './index.ts',
}
export const setup = {
    name:'draco3d',
    assetId:'ZHJhY28zZA==',
    version:'1.5.7',
    shortDescription:"Draco is a library for compressing and decompressing 3D geometric meshes and point clouds. It is intended to improve the storage and transmission of 3D graphics.",
    apiVersion:'1',
    runTimeDependencies,
    externals,
    exportedSymbols,
    entries,
}

