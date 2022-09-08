import * as AllImports from "d3";
import DefaultImport from "d3";

export * from "d3";
export default DefaultImport;
// Pick the right one and remove useless import
window["d3_APIv5"] = DefaultImport || AllImports;
