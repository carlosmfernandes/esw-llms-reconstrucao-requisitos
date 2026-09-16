import { normalizeDates } from "../_lib/normalizeDates/index.ts";
import { startOfWeek } from "../startOfWeek/index.ts";
import type { LocalizedOptions, WeekOptions } from "../types.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface IsSameWeekOptions
  extends WeekOptions, LocalizedOptions<"options">, ContextOptions<Date> {}

export function isSameWeek(
  laterDate: DateArg<Date> & {},
  earlierDate: DateArg<Date> & {},
  options?: IsSameWeekOptions,
): boolean {
  const [laterDate_, earlierDate_] = normalizeDates(
    options?.in,
    laterDate,
    earlierDate,
  );
  return (
    +startOfWeek(laterDate_, options) === +startOfWeek(earlierDate_, options)
  );
}
