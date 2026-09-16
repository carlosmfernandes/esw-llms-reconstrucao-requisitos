import { defaultLocale } from "../_lib/defaultLocale/index.ts";
import { getDefaultOptions } from "../_lib/defaultOptions/index.ts";
import { normalizeDates } from "../_lib/normalizeDates/index.ts";
import { differenceInCalendarDays } from "../differenceInCalendarDays/index.ts";
import { format } from "../format/index.ts";
import type { FormatRelativeToken } from "../locale/types.ts";
import type {
  ContextOptions,
  DateArg,
  LocalizedOptions,
  WeekOptions,
} from "../types.ts";

export interface FormatRelativeOptions
  extends
    LocalizedOptions<"options" | "localize" | "formatLong" | "formatRelative">,
    WeekOptions,
    ContextOptions<Date> {}

export function formatRelative(
  date: DateArg<Date> & {},
  baseDate: DateArg<Date> & {},
  options?: FormatRelativeOptions,
): string {
  const [date_, baseDate_] = normalizeDates(options?.in, date, baseDate);

  const defaultOptions = getDefaultOptions();
  const locale = options?.locale ?? defaultOptions.locale ?? defaultLocale;
  const weekStartsOn =
    options?.weekStartsOn ??
    options?.locale?.options?.weekStartsOn ??
    defaultOptions.weekStartsOn ??
    defaultOptions.locale?.options?.weekStartsOn ??
    0;

  const diff = differenceInCalendarDays(date_, baseDate_);

  if (isNaN(diff)) {
    throw new RangeError("Invalid time value");
  }

  let token: FormatRelativeToken;
  if (diff < -6) {
    token = "other";
  } else if (diff < -1) {
    token = "lastWeek";
  } else if (diff < 0) {
    token = "yesterday";
  } else if (diff < 1) {
    token = "today";
  } else if (diff < 2) {
    token = "tomorrow";
  } else if (diff < 7) {
    token = "nextWeek";
  } else {
    token = "other";
  }

  const formatStr = locale.formatRelative(token, date_, baseDate_, {
    locale,
    weekStartsOn,
  });
  return format(date_, formatStr, { locale, weekStartsOn });
}
