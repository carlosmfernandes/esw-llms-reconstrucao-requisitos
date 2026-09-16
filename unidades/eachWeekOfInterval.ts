import { normalizeInterval } from "../_lib/normalizeInterval/index.ts";
import { addWeeks } from "../addWeeks/index.ts";
import { constructFrom } from "../constructFrom/index.ts";
import { startOfWeek } from "../startOfWeek/index.ts";
import type {
  ContextOptions,
  Interval,
  LocalizedOptions,
  StepOptions,
  WeekOptions,
} from "../types.ts";

export interface EachWeekOfIntervalOptions<DateType extends Date = Date>
  extends
    StepOptions,
    WeekOptions,
    LocalizedOptions<"options">,
    ContextOptions<DateType> {}

export type EachWeekOfIntervalResult<
  IntervalType extends Interval,
  Options extends EachWeekOfIntervalOptions | undefined,
> = Array<
  Options extends EachWeekOfIntervalOptions<infer DateType>
    ? DateType
    : IntervalType["start"] extends Date
      ? IntervalType["start"]
      : IntervalType["end"] extends Date
        ? IntervalType["end"]
        : Date
>;

export function eachWeekOfInterval<
  IntervalType extends Interval,
  Options extends EachWeekOfIntervalOptions | undefined = undefined,
>(
  interval: IntervalType,
  options?: Options,
): EachWeekOfIntervalResult<IntervalType, Options> {
  const { start, end } = normalizeInterval(options?.in, interval);

  let reversed = +start > +end;
  const startDateWeek = reversed
    ? startOfWeek(end, options)
    : startOfWeek(start, options);
  const endDateWeek = reversed
    ? startOfWeek(start, options)
    : startOfWeek(end, options);

  startDateWeek.setHours(15);
  endDateWeek.setHours(15);

  const endTime = +endDateWeek.getTime();
  let currentDate = startDateWeek;

  let step = options?.step ?? 1;
  if (!step) return [];
  if (step < 0) {
    step = -step;
    reversed = !reversed;
  }

  const dates: EachWeekOfIntervalResult<IntervalType, Options> = [];

  while (+currentDate <= endTime) {
    currentDate.setHours(0);
    dates.push(constructFrom(start, currentDate));
    currentDate = addWeeks(currentDate, step);
    currentDate.setHours(15);
  }

  return reversed ? dates.reverse() : dates;
}
