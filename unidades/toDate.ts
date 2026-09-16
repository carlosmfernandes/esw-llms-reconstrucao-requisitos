import { constructFrom } from "../constructFrom/index.ts";
import type { ConstructableDate, ContextFn, DateArg } from "../types.ts";

export function toDate<
  DateType extends Date | ConstructableDate,
  ResultDate extends Date = DateType,
>(
  argument: DateArg<DateType>,
  context?: ContextFn<ResultDate> | undefined,
): ResultDate {
  // [TODO] Get rid of `toDate` or `constructFrom`?
  return constructFrom(context || argument, argument);
}
