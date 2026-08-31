from typing import Literal

ApiV1ConditionsArchiveCreateSeverityErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONDITIONS_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionsArchiveCreateSeverityErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_conditions_archive_create_severity_error_component_code(
    value: str,
) -> ApiV1ConditionsArchiveCreateSeverityErrorComponentCode:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
