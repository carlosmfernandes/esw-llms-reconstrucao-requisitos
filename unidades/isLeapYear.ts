import { toDate } from "../toDate/index.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface IsLeapYearOptions extends ContextOptions<Date> {}

export function isLeapYear(
  date: DateArg<Date> & {},
  options?: IsLeapYearOptions | undefined,
): boolean {
  const _date = toDate(date, options?.in);
  const year = _date.getFullYear();
  return year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0);
}
