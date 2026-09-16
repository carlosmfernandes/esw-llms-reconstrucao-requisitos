import { normalizeDates } from "../_lib/normalizeDates/index.ts";
import { startOfDay } from "../startOfDay/index.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface IsSameDayOptions extends ContextOptions<Date> {}

export function isSameDay(
  laterDate: DateArg<Date> & {},
  earlierDate: DateArg<Date> & {},
  options?: IsSameDayOptions | undefined,
): boolean {
  const [dateLeft_, dateRight_] = normalizeDates(
    options?.in,
    laterDate,
    earlierDate,
  );
  return +startOfDay(dateLeft_) === +startOfDay(dateRight_);
}
