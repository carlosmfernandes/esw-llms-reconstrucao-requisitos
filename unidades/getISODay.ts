import { toDate } from "../toDate/index.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface GetISODayOptions extends ContextOptions<Date> {}

export function getISODay(
  date: DateArg<Date> & {},
  options?: GetISODayOptions,
): number {
  const day = toDate(date, options?.in).getDay();
  return day === 0 ? 7 : day;
}
