from typing import Literal

DowntimeRequestKind = Literal[
    "customer-caused",
    "emergency-maintenance",
    "false-positive",
    "force-majeure",
    "generic",
    "planned-maintenance",
    "upstream-provider",
]

DOWNTIME_REQUEST_KIND_VALUES: set[DowntimeRequestKind] = {
    "customer-caused",
    "emergency-maintenance",
    "false-positive",
    "force-majeure",
    "generic",
    "planned-maintenance",
    "upstream-provider",
}


def check_downtime_request_kind(value: str) -> DowntimeRequestKind:
    if value in DOWNTIME_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOWNTIME_REQUEST_KIND_VALUES!r}")
