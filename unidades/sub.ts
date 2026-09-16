import { constructFrom } from "../constructFrom/index.ts";
import { subDays } from "../subDays/index.ts";
import { subMonths } from "../subMonths/index.ts";
import type { ContextOptions, DateArg, Duration } from "../types.ts";

export interface SubOptions<
  DateType extends Date = Date,
> extends ContextOptions<DateType> {}

export function sub<DateType extends Date, ResultDate extends Date = DateType>(
  date: DateArg<DateType>,
  duration: Duration,
  options?: SubOptions<ResultDate>,
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

  const withoutMonths = subMonths(date, months + years * 12, options);
  const withoutDays = subDays(withoutMonths, days + weeks * 7, options);

  const minutesToSub = minutes + hours * 60;
  const secondsToSub = seconds + minutesToSub * 60;
  const msToSub = secondsToSub * 1000;

  return constructFrom(options?.in || date, +withoutDays - msToSub);
}
