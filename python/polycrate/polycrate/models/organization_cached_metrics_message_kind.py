from typing import Literal

OrganizationCachedMetricsMessageKind = Literal["downtime", "incident", "maintenance"]

ORGANIZATION_CACHED_METRICS_MESSAGE_KIND_VALUES: set[OrganizationCachedMetricsMessageKind] = {
    "downtime",
    "incident",
    "maintenance",
}


def check_organization_cached_metrics_message_kind(value: str) -> OrganizationCachedMetricsMessageKind:
    if value in ORGANIZATION_CACHED_METRICS_MESSAGE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_CACHED_METRICS_MESSAGE_KIND_VALUES!r}")
