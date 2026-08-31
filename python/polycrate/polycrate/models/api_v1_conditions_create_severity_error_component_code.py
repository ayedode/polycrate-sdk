from typing import Literal

ApiV1ConditionsCreateSeverityErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONDITIONS_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ConditionsCreateSeverityErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_conditions_create_severity_error_component_code(
    value: str,
) -> ApiV1ConditionsCreateSeverityErrorComponentCode:
    if value in API_V1_CONDITIONS_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
