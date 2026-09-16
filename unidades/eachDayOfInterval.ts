import { normalizeInterval } from "../_lib/normalizeInterval/index.ts";
import { constructFrom } from "../constructFrom/index.ts";
import type { ContextOptions, Interval, StepOptions } from "../types.ts";

export interface EachDayOfIntervalOptions<DateType extends Date = Date>
  extends StepOptions, ContextOptions<DateType> {}

export type EachDayOfIntervalResult<
  IntervalType extends Interval,
  Options extends EachDayOfIntervalOptions | undefined,
> = Array<
  Options extends EachDayOfIntervalOptions<infer DateType>
    ? DateType
    : IntervalType["start"] extends Date
      ? IntervalType["start"]
      : IntervalType["end"] extends Date
        ? IntervalType["end"]
        : Date
>;

export function eachDayOfInterval<
  IntervalType extends Interval,
  Options extends EachDayOfIntervalOptions | undefined = undefined,
>(
  interval: IntervalType,
  options?: Options,
): EachDayOfIntervalResult<IntervalType, Options> {
  const { start, end } = normalizeInterval(options?.in, interval);

  let reversed = +start > +end;
  const endTime = reversed ? +start : +end;
  const date = reversed ? end : start;
  date.setHours(0, 0, 0, 0);

  let step = options?.step ?? 1;
  if (!step) return [];
  if (step < 0) {
    step = -step;
    reversed = !reversed;
  }

  const dates: EachDayOfIntervalResult<IntervalType, Options> = [];

  while (+date <= endTime) {
    dates.push(constructFrom(start, date));
    date.setDate(date.getDate() + step);
    date.setHours(0, 0, 0, 0);
  }

  return reversed ? dates.reverse() : dates;
}
