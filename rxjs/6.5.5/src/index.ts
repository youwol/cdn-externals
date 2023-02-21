export * from "rxjs";
export * as operators from "rxjs/operators";
export * as fetch from "rxjs/fetch";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";
import * as fetch from "rxjs/fetch";

window["rxjs_APIv6"] = { ...rxjs, operators, fetch };
