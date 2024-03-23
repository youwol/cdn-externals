import * as AllImports from "pyodide";

export * from "pyodide";

export function loadPyodideCustom(args) {
  return AllImports.loadPyodide(args);
}
