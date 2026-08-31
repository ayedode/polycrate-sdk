from typing import Literal

ApiV1CvesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_CVES_LIST_STATE_VALUES: set[ApiV1CvesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_cves_list_state(value: str) -> ApiV1CvesListState:
    if value in API_V1_CVES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_STATE_VALUES!r}")
