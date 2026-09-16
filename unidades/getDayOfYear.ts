import { differenceInCalendarDays } from "../differenceInCalendarDays/index.ts";
import { startOfYear } from "../startOfYear/index.ts";
import { toDate } from "../toDate/index.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface GetDayOfYearOptions extends ContextOptions<Date> {}

export function getDayOfYear(
  date: DateArg<Date> & {},
  options?: GetDayOfYearOptions | undefined,
): number {
  const _date = toDate(date, options?.in);
  const diff = differenceInCalendarDays(_date, startOfYear(_date));
  const dayOfYear = diff + 1;
  return dayOfYear;
}
