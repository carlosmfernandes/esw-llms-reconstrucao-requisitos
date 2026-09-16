import { isDate } from "../isDate/index.ts";
import { toDate } from "../toDate/index.ts";

export function isValid(date: unknown): boolean {
  return !((!isDate(date) && typeof date !== "number") || isNaN(+toDate(date)));
}
