import * as AllImports from "bootstrap";
import DefaultImport from "bootstrap";

export * from "bootstrap";
export default DefaultImport;
// Pick the right one and remove useless import
window["bootstrap_APIv4"] = DefaultImport || AllImports;
