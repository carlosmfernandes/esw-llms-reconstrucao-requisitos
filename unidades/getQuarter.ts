import { toDate } from "../toDate/index.ts";
import type { ContextOptions, DateArg } from "../types.ts";

export interface GetQuarterOptions extends ContextOptions<Date> {}

export function getQuarter(
  date: DateArg<Date> & {},
  options?: GetQuarterOptions | undefined,
): number {
  const _date = toDate(date, options?.in);
  const quarter = Math.trunc(_date.getMonth() / 3) + 1;
  return quarter;
}
