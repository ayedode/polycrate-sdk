from typing import Literal

ApiV1ConditionsListSeverity = Literal["critical", "info", "warning"]

API_V1_CONDITIONS_LIST_SEVERITY_VALUES: set[ApiV1ConditionsListSeverity] = {
    "critical",
    "info",
    "warning",
}


def check_api_v1_conditions_list_severity(value: str) -> ApiV1ConditionsListSeverity:
    if value in API_V1_CONDITIONS_LIST_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_LIST_SEVERITY_VALUES!r}")
