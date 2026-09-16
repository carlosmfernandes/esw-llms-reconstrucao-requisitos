import { normalizeDates } from "../_lib/normalizeDates/index.ts";
import { addDays } from "../addDays/index.ts";
import { differenceInCalendarDays } from "../differenceInCalendarDays/index.ts";
import { isSameDay } from "../isSameDay/index.ts";
import { isValid } from "../isValid/index.ts";
import { isWeekend } from "../isWeekend/index.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface DifferenceInBusinessDaysOptions extends ContextOptions<Date> {}

export function differenceInBusinessDays(
  laterDate: DateArg<Date> & {},
  earlierDate: DateArg<Date> & {},
  options?: DifferenceInBusinessDaysOptions | undefined,
): number {
  const [laterDate_, earlierDate_] = normalizeDates(
    options?.in,
    laterDate,
    earlierDate,
  );

  if (!isValid(laterDate_) || !isValid(earlierDate_)) return NaN;

  const diff = differenceInCalendarDays(laterDate_, earlierDate_);
  const sign = diff < 0 ? -1 : 1;
  const weeks = Math.trunc(diff / 7);

  let result = weeks * 5;
  let movingDate = addDays(earlierDate_, weeks * 7);

  // the loop below will run at most 6 times to account for the remaining days that don't makeup a full week
  while (!isSameDay(laterDate_, movingDate)) {
    // sign is used to account for both negative and positive differences
    result += isWeekend(movingDate, options) ? 0 : sign;
    movingDate = addDays(movingDate, sign);
  }

  // Prevent negative zero
  return result === 0 ? 0 : result;
}
