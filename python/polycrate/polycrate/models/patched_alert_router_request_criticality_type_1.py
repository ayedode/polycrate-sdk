from typing import Literal

PatchedAlertRouterRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_ALERT_ROUTER_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedAlertRouterRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_alert_router_request_criticality_type_1(value: str) -> PatchedAlertRouterRequestCriticalityType1:
    if value in PATCHED_ALERT_ROUTER_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ALERT_ROUTER_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
