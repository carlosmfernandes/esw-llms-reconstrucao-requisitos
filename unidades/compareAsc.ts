import { toDate } from "../toDate/index.ts";
import type { DateArg } from "../types.ts";

export function compareAsc(
  dateLeft: DateArg<Date> & {},
  dateRight: DateArg<Date> & {},
): number {
  const diff = +toDate(dateLeft) - +toDate(dateRight);

  if (diff < 0) return -1;
  else if (diff > 0) return 1;

  // Return 0 if diff is 0; return NaN if diff is NaN
  return diff;
}
