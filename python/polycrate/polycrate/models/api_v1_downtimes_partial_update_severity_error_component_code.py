from typing import Literal

ApiV1DowntimesPartialUpdateSeverityErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesPartialUpdateSeverityErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_downtimes_partial_update_severity_error_component_code(
    value: str,
) -> ApiV1DowntimesPartialUpdateSeverityErrorComponentCode:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
