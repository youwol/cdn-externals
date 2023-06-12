import {Point, Proj, WGS84,  mgrs, nadgrid, toPoint} from "proj4";
import DefaultImport from "proj4";
import * as toto from "proj4"
console.log("Default Import", {DefaultImport, toto, defs:DefaultImport.defs} )
//export * from "proj4";
export let defs = DefaultImport.defs;
//window['proj4'] = DefaultImport