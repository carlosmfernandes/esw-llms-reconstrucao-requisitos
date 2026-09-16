import { getTimezoneOffsetInMilliseconds } from "../_lib/getTimezoneOffsetInMilliseconds/index.ts";
import { millisecondsInDay } from "../constants/index.ts";
import { toDate } from "../toDate/index.ts";
import type { Interval } from "../types.ts";

export function getOverlappingDaysInIntervals(
  intervalLeft: Interval,
  intervalRight: Interval,
): number {
  const [leftStart, leftEnd] = [
    +toDate(intervalLeft.start),
    +toDate(intervalLeft.end),
  ].sort((a, b) => a - b);
  const [rightStart, rightEnd] = [
    +toDate(intervalRight.start),
    +toDate(intervalRight.end),
  ].sort((a, b) => a - b);

  // Prevent NaN result if intervals don't overlap at all.
  const isOverlapping = leftStart < rightEnd && rightStart < leftEnd;
  if (!isOverlapping) return 0;

  // Remove the timezone offset to negate the DST effect on calculations.
  const overlapLeft = rightStart < leftStart ? leftStart : rightStart;
  const left = overlapLeft - getTimezoneOffsetInMilliseconds(overlapLeft);
  const overlapRight = rightEnd > leftEnd ? leftEnd : rightEnd;
  const right = overlapRight - getTimezoneOffsetInMilliseconds(overlapRight);

  // Ceil the number to include partial days too.
  return Math.ceil((right - left) / millisecondsInDay);
}
