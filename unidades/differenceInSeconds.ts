import { getRoundingMethod } from "../_lib/getRoundingMethod/index.ts";
import { differenceInMilliseconds } from "../differenceInMilliseconds/index.ts";
import type { DateArg, RoundingOptions } from "../types.ts";

export interface DifferenceInSecondsOptions extends RoundingOptions {}

export function differenceInSeconds(
  laterDate: DateArg<Date> & {},
  earlierDate: DateArg<Date> & {},
  options?: DifferenceInSecondsOptions,
): number {
  const diff = differenceInMilliseconds(laterDate, earlierDate) / 1000;
  return getRoundingMethod(options?.roundingMethod)(diff);
}
