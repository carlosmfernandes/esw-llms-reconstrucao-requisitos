import { toDate } from "../toDate/index.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface IsWeekendOptions extends ContextOptions<Date> {}

export function isWeekend(
  date: DateArg<Date> & {},
  options?: IsWeekendOptions | undefined,
): boolean {
  const day = toDate(date, options?.in).getDay();
  return day === 0 || day === 6;
}
