from typing import Literal

PatchedDowntimeRequestKind = Literal[
    "customer-caused",
    "emergency-maintenance",
    "false-positive",
    "force-majeure",
    "generic",
    "planned-maintenance",
    "upstream-provider",
]

PATCHED_DOWNTIME_REQUEST_KIND_VALUES: set[PatchedDowntimeRequestKind] = {
    "customer-caused",
    "emergency-maintenance",
    "false-positive",
    "force-majeure",
    "generic",
    "planned-maintenance",
    "upstream-provider",
}


def check_patched_downtime_request_kind(value: str) -> PatchedDowntimeRequestKind:
    if value in PATCHED_DOWNTIME_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_DOWNTIME_REQUEST_KIND_VALUES!r}")
