import { normalizeInterval } from "../_lib/normalizeInterval/index.ts";
import { add } from "../add/index.ts";
import { differenceInDays } from "../differenceInDays/index.ts";
import { differenceInHours } from "../differenceInHours/index.ts";
import { differenceInMinutes } from "../differenceInMinutes/index.ts";
import { differenceInMonths } from "../differenceInMonths/index.ts";
import { differenceInSeconds } from "../differenceInSeconds/index.ts";
import { differenceInYears } from "../differenceInYears/index.ts";
import type { ContextOptions, Duration, Interval } from "../types.ts";

export interface IntervalToDurationOptions extends ContextOptions<Date> {}

export function intervalToDuration(
  interval: Interval,
  options?: IntervalToDurationOptions | undefined,
): Duration {
  const { start, end } = normalizeInterval(options?.in, interval);
  const duration: Duration = {};

  const years = differenceInYears(end, start);
  if (years) duration.years = years;

  const remainingMonths = add(start, { years: duration.years });
  const months = differenceInMonths(end, remainingMonths);
  if (months) duration.months = months;

  const remainingDays = add(remainingMonths, { months: duration.months });
  const days = differenceInDays(end, remainingDays);
  if (days) duration.days = days;

  const remainingHours = add(remainingDays, { days: duration.days });
  const hours = differenceInHours(end, remainingHours);
  if (hours) duration.hours = hours;

  const remainingMinutes = add(remainingHours, { hours: duration.hours });
  const minutes = differenceInMinutes(end, remainingMinutes);
  if (minutes) duration.minutes = minutes;

  const remainingSeconds = add(remainingMinutes, { minutes: duration.minutes });
  const seconds = differenceInSeconds(end, remainingSeconds);
  if (seconds) duration.seconds = seconds;

  return duration;
}
