import * as AllImports from "plotly.js-gl2d-dist";
import DefaultImport from "plotly.js-gl2d-dist";

export * from "plotly.js-gl2d-dist";
export default DefaultImport;
// Pick the right one and remove useless import
window["Plotly_APIv2"] = DefaultImport || AllImports;
