import { constructFrom } from "../constructFrom/index.ts";
import { toDate } from "../toDate/index.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface SetYearOptions<
  DateType extends Date = Date,
> extends ContextOptions<DateType> {}

export function setYear<
  DateType extends Date,
  ResultDate extends Date = DateType,
>(
  date: DateArg<DateType>,
  year: number,
  options?: SetYearOptions<ResultDate> | undefined,
): ResultDate {
  const date_ = toDate(date, options?.in);

  // Check if date is Invalid Date because Date.prototype.setFullYear ignores the value of Invalid Date
  if (isNaN(+date_)) return constructFrom(options?.in || date, NaN);

  date_.setFullYear(year);
  return date_;
}
