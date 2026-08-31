from typing import Literal

ApiV1DowntimesCreateSeverityErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOWNTIMES_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DowntimesCreateSeverityErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_downtimes_create_severity_error_component_code(
    value: str,
) -> ApiV1DowntimesCreateSeverityErrorComponentCode:
    if value in API_V1_DOWNTIMES_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
