import { normalizeDates } from "../_lib/normalizeDates/index.ts";
import { max } from "../max/index.ts";
import { min } from "../min/index.ts";
import type { ContextOptions, DateArg, Interval } from "../types.ts";

export interface ClampOptions<
  ContextDate extends Date = Date,
> extends ContextOptions<ContextDate> {}

export type ClampResult<
  DateType extends DateArg<Date>,
  IntervalType extends Interval,
  Options extends ClampOptions | undefined,
> =
  Options extends ClampOptions<infer DateType extends Date>
    ? DateType
    : DateType extends Date
      ? DateType
      : IntervalType["start"] extends Date
        ? IntervalType["start"]
        : IntervalType["end"] extends Date
          ? IntervalType["end"]
          : Date;

export function clamp<
  DateType extends DateArg<Date>,
  IntervalType extends Interval,
  Options extends ClampOptions | undefined = undefined,
>(
  date: DateType,
  interval: IntervalType,
  options?: Options,
): ClampResult<DateType, IntervalType, Options> {
  const [date_, start, end] = normalizeDates(
    options?.in,
    date,
    interval.start,
    interval.end,
  );

  return min([max([date_, start], options), end], options) as ClampResult<
    DateType,
    IntervalType,
    Options
  >;
}
