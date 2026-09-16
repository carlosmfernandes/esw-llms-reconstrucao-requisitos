import { getDefaultOptions } from "../_lib/defaultOptions/index.ts";
import { toDate } from "../toDate/index.ts";
import type {
  ContextOptions,
  DateArg,
  LocalizedOptions,
  WeekOptions,
} from "../types.ts";

export interface StartOfWeekOptions<DateType extends Date = Date>
  extends LocalizedOptions<"options">, WeekOptions, ContextOptions<DateType> {}

export function startOfWeek<
  DateType extends Date,
  ResultDate extends Date = DateType,
>(
  date: DateArg<DateType>,
  options?: StartOfWeekOptions<ResultDate>,
): ResultDate {
  const defaultOptions = getDefaultOptions();
  const weekStartsOn =
    options?.weekStartsOn ??
    options?.locale?.options?.weekStartsOn ??
    defaultOptions.weekStartsOn ??
    defaultOptions.locale?.options?.weekStartsOn ??
    0;

  const _date = toDate(date, options?.in);
  const day = _date.getDay();
  const diff = (day < weekStartsOn ? 7 : 0) + day - weekStartsOn;

  _date.setDate(_date.getDate() - diff);
  _date.setHours(0, 0, 0, 0);
  return _date;
}
