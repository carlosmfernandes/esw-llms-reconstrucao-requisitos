import { constructFrom } from "../constructFrom/index.ts";
import { isSaturday } from "../isSaturday/index.ts";
import { isSunday } from "../isSunday/index.ts";
import { isWeekend } from "../isWeekend/index.ts";
import { toDate } from "../toDate/index.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface AddBusinessDaysOptions<
  DateType extends Date = Date,
> extends ContextOptions<DateType> {}

export function addBusinessDays<
  DateType extends Date,
  ResultDate extends Date = DateType,
>(
  date: DateArg<DateType>,
  amount: number,
  options?: AddBusinessDaysOptions<ResultDate> | undefined,
): ResultDate {
  const _date = toDate(date, options?.in);
  const startedOnWeekend = isWeekend(_date, options);

  if (isNaN(amount)) return constructFrom(options?.in, NaN);

  const hours = _date.getHours();
  const sign = amount < 0 ? -1 : 1;
  const fullWeeks = Math.trunc(amount / 5);

  _date.setDate(_date.getDate() + fullWeeks * 7);

  // Get remaining days not part of a full week
  let restDays = Math.abs(amount % 5);

  // Loops over remaining days
  while (restDays > 0) {
    _date.setDate(_date.getDate() + sign);
    if (!isWeekend(_date, options)) restDays -= 1;
  }

  // If the date is a weekend day and we reduce a dividable of
  // 5 from it, we land on a weekend date.
  // To counter this, we add days accordingly to land on the next business day
  if (startedOnWeekend && isWeekend(_date, options) && amount !== 0) {
    // If we're reducing days, we want to add days until we land on a weekday
    // If we're adding days we want to reduce days until we land on a weekday
    if (isSaturday(_date, options))
      _date.setDate(_date.getDate() + (sign < 0 ? 2 : -1));
    if (isSunday(_date, options))
      _date.setDate(_date.getDate() + (sign < 0 ? 1 : -2));
  }

  // Restore hours to avoid DST lag
  _date.setHours(hours);

  return _date;
}
