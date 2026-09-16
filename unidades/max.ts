import { constructFrom } from "../constructFrom/index.ts";
import { toDate } from "../toDate/index.ts";
import type { ContextFn, ContextOptions, DateArg } from "../types.ts";

export interface MaxOptions<
  DateType extends Date = Date,
> extends ContextOptions<DateType> {}

export function max<DateType extends Date, ResultDate extends Date = DateType>(
  dates: DateArg<DateType>[],
  options?: MaxOptions<ResultDate> | undefined,
): ResultDate {
  let result: ResultDate | undefined;
  let context = options?.in;

  dates.forEach((date) => {
    // Use the first date object as the context function
    if (!context && typeof date === "object")
      context = constructFrom.bind(null, date) as ContextFn<ResultDate>;

    const date_ = toDate(date, context);
    if (!result || result < date_ || isNaN(+date_)) result = date_;
  });

  return constructFrom(context, result || NaN);
}
