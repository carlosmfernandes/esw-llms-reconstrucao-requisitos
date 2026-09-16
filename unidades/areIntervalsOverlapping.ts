import { toDate } from "../toDate/index.ts";
import type { ContextOptions, Interval } from "../types.ts";

export interface AreIntervalsOverlappingOptions extends ContextOptions<Date> {
  inclusive?: boolean;
}

export function areIntervalsOverlapping(
  intervalLeft: Interval,
  intervalRight: Interval,
  options?: AreIntervalsOverlappingOptions,
): boolean {
  const [leftStartTime, leftEndTime] = [
    +toDate(intervalLeft.start, options?.in),
    +toDate(intervalLeft.end, options?.in),
  ].sort((a, b) => a - b);
  const [rightStartTime, rightEndTime] = [
    +toDate(intervalRight.start, options?.in),
    +toDate(intervalRight.end, options?.in),
  ].sort((a, b) => a - b);

  if (options?.inclusive)
    return leftStartTime <= rightEndTime && rightStartTime <= leftEndTime;

  return leftStartTime < rightEndTime && rightStartTime < leftEndTime;
}
