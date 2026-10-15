from typing import Literal

PatchedAlertRequestKind = Literal["checkmk", "generic", "grafana"]

PATCHED_ALERT_REQUEST_KIND_VALUES: set[PatchedAlertRequestKind] = {
    "checkmk",
    "generic",
    "grafana",
}


def check_patched_alert_request_kind(value: str) -> PatchedAlertRequestKind:
    if value in PATCHED_ALERT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ALERT_REQUEST_KIND_VALUES!r}")
