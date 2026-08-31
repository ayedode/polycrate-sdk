from typing import Literal

OrganizationCachedMetricsMessageKindEnum = Literal["downtime", "incident", "maintenance"]

ORGANIZATION_CACHED_METRICS_MESSAGE_KIND_ENUM_VALUES: set[OrganizationCachedMetricsMessageKindEnum] = {
    "downtime",
    "incident",
    "maintenance",
}


def check_organization_cached_metrics_message_kind_enum(value: str) -> OrganizationCachedMetricsMessageKindEnum:
    if value in ORGANIZATION_CACHED_METRICS_MESSAGE_KIND_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_CACHED_METRICS_MESSAGE_KIND_ENUM_VALUES!r}"
    )
