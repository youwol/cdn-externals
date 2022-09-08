// export * from "lodash";
// import lodash from 'lodash'
// export default lodash;
import * as AllImports from "lodash";
import DefaultImport from "lodash";

export * from "lodash";
export default DefaultImport;
window["__APIv4"] = DefaultImport || AllImports;
