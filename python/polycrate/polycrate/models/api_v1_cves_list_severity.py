from typing import Literal

ApiV1CvesListSeverity = Literal["critical", "high", "low", "medium", "none", "unknown"]

API_V1_CVES_LIST_SEVERITY_VALUES: set[ApiV1CvesListSeverity] = {
    "critical",
    "high",
    "low",
    "medium",
    "none",
    "unknown",
}


def check_api_v1_cves_list_severity(value: str) -> ApiV1CvesListSeverity:
    if value in API_V1_CVES_LIST_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_SEVERITY_VALUES!r}")
