from typing import Literal

PatchedRegionRequestState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PATCHED_REGION_REQUEST_STATE_VALUES: set[PatchedRegionRequestState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_patched_region_request_state(value: str) -> PatchedRegionRequestState:
    if value in PATCHED_REGION_REQUEST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_REGION_REQUEST_STATE_VALUES!r}")
