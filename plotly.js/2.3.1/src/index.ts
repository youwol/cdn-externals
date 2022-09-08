import * as AllImports from "plotly.js";
import DefaultImport from "plotly.js";

export * from "plotly.js";
export default DefaultImport;
// Pick the right one and remove useless import
window["Plotly_APIv2"] = DefaultImport || AllImports;
