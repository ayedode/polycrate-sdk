from typing import Literal

ApiV1CvesListStatus = Literal["disputed", "open", "rejected", "reserved"]

API_V1_CVES_LIST_STATUS_VALUES: set[ApiV1CvesListStatus] = {
    "disputed",
    "open",
    "rejected",
    "reserved",
}


def check_api_v1_cves_list_status(value: str) -> ApiV1CvesListStatus:
    if value in API_V1_CVES_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_STATUS_VALUES!r}")
