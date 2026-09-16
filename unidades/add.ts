import { addDays } from "../addDays/index.ts";
import { addMonths } from "../addMonths/index.ts";
import { constructFrom } from "../constructFrom/index.ts";
import { toDate } from "../toDate/index.ts";
import type { ContextOptions, DateArg, Duration } from "../types.ts";

export interface AddOptions<
  DateType extends Date = Date,
> extends ContextOptions<DateType> {}

export function add<DateType extends Date, ResultDate extends Date = DateType>(
  date: DateArg<DateType>,
  duration: Duration,
  options?: AddOptions<ResultDate> | undefined,
): ResultDate {
  const {
    years = 0,
    months = 0,
    weeks = 0,
    days = 0,
    hours = 0,
    minutes = 0,
    seconds = 0,
  } = duration;

  // Add years and months
  const _date = toDate(date, options?.in);
  const dateWithMonths =
    months || years ? addMonths(_date, months + years * 12) : _date;

  // Add weeks and days
  const dateWithDays =
    days || weeks ? addDays(dateWithMonths, days + weeks * 7) : dateWithMonths;

  // Add days, hours, minutes, and seconds
  const minutesToAdd = minutes + hours * 60;
  const secondsToAdd = seconds + minutesToAdd * 60;
  const msToAdd = secondsToAdd * 1000;

  return constructFrom(options?.in || date, +dateWithDays + msToAdd);
}
