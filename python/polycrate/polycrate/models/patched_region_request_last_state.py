from typing import Literal

PatchedRegionRequestLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PATCHED_REGION_REQUEST_LAST_STATE_VALUES: set[PatchedRegionRequestLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_patched_region_request_last_state(value: str) -> PatchedRegionRequestLastState:
    if value in PATCHED_REGION_REQUEST_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_REGION_REQUEST_LAST_STATE_VALUES!r}")
