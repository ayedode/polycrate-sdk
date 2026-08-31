from typing import Literal

ApiV1CvesListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_CVES_LIST_STATE_NOT_VALUES: set[ApiV1CvesListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_cves_list_state_not(value: str) -> ApiV1CvesListStateNot:
    if value in API_V1_CVES_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_STATE_NOT_VALUES!r}")
