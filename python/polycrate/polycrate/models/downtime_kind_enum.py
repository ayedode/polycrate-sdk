from typing import Literal

DowntimeKindEnum = Literal[
    "customer-caused",
    "emergency-maintenance",
    "false-positive",
    "force-majeure",
    "generic",
    "planned-maintenance",
    "upstream-provider",
]

DOWNTIME_KIND_ENUM_VALUES: set[DowntimeKindEnum] = {
    "customer-caused",
    "emergency-maintenance",
    "false-positive",
    "force-majeure",
    "generic",
    "planned-maintenance",
    "upstream-provider",
}


def check_downtime_kind_enum(value: str) -> DowntimeKindEnum:
    if value in DOWNTIME_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOWNTIME_KIND_ENUM_VALUES!r}")
