import * as AllImports from "tslib";
import DefaultImport from "tslib";

export * from "tslib";
export default DefaultImport;
// Pick the right one and remove useless import
window["tslib_APIv1"] = DefaultImport || AllImports;
