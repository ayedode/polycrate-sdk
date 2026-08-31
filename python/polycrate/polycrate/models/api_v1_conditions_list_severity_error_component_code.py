from typing import Literal

ApiV1ConditionsListSeverityErrorComponentCode = Literal["invalid_choice"]

API_V1_CONDITIONS_LIST_SEVERITY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ConditionsListSeverityErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_conditions_list_severity_error_component_code(
    value: str,
) -> ApiV1ConditionsListSeverityErrorComponentCode:
    if value in API_V1_CONDITIONS_LIST_SEVERITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_LIST_SEVERITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
