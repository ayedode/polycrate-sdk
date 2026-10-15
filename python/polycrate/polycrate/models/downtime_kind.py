from typing import Literal

DowntimeKind = Literal[
    "customer-caused",
    "emergency-maintenance",
    "false-positive",
    "force-majeure",
    "generic",
    "planned-maintenance",
    "upstream-provider",
]

DOWNTIME_KIND_VALUES: set[DowntimeKind] = {
    "customer-caused",
    "emergency-maintenance",
    "false-positive",
    "force-majeure",
    "generic",
    "planned-maintenance",
    "upstream-provider",
}


def check_downtime_kind(value: str) -> DowntimeKind:
    if value in DOWNTIME_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOWNTIME_KIND_VALUES!r}")
