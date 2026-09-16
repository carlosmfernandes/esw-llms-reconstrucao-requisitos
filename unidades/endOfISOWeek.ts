import { endOfWeek } from "../endOfWeek/index.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface EndOfISOWeekOptions<
  DateType extends Date = Date,
> extends ContextOptions<DateType> {}

export function endOfISOWeek<
  DateType extends Date,
  ResultDate extends Date = DateType,
>(
  date: DateArg<DateType>,
  options?: EndOfISOWeekOptions<ResultDate> | undefined,
): ResultDate {
  return endOfWeek(date, { ...options, weekStartsOn: 1 });
}
