from typing import Literal

ApiV1CvesPartialUpdateSeverityErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CVES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CvesPartialUpdateSeverityErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_cves_partial_update_severity_error_component_code(
    value: str,
) -> ApiV1CvesPartialUpdateSeverityErrorComponentCode:
    if value in API_V1_CVES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
