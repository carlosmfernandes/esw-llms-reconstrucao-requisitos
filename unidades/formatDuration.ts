import type { FormatDistanceToken } from "../locale/types.ts";
import type { Duration, DurationUnit, LocalizedOptions } from "../types.ts";
import { defaultLocale } from "../_lib/defaultLocale/index.ts";
import { getDefaultOptions } from "../_lib/defaultOptions/index.ts";

export interface FormatDurationOptions extends LocalizedOptions<"formatDistance"> {
  format?: DurationUnit[];
  zero?: boolean;
  delimiter?: string;
}

const defaultFormat: DurationUnit[] = [
  "years",
  "months",
  "weeks",
  "days",
  "hours",
  "minutes",
  "seconds",
];

export function formatDuration(
  duration: Duration,
  options?: FormatDurationOptions,
): string {
  const defaultOptions = getDefaultOptions();
  const locale = options?.locale ?? defaultOptions.locale ?? defaultLocale;
  const format = options?.format ?? defaultFormat;
  const zero = options?.zero ?? false;
  const delimiter = options?.delimiter ?? " ";

  if (!locale.formatDistance) {
    return "";
  }

  const result = format
    .reduce((acc, unit) => {
      const token = `x${unit.replace(/(^.)/, (m) =>
        m.toUpperCase(),
      )}` as FormatDistanceToken;
      const value = duration[unit];
      if (value !== undefined && (zero || duration[unit])) {
        return acc.concat(locale.formatDistance(token, value));
      }
      return acc;
    }, [] as string[])
    .join(delimiter);

  return result;
}
