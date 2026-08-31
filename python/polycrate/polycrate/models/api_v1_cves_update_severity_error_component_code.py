from typing import Literal

ApiV1CvesUpdateSeverityErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CVES_UPDATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesUpdateSeverityErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_cves_update_severity_error_component_code(value: str) -> ApiV1CvesUpdateSeverityErrorComponentCode:
    if value in API_V1_CVES_UPDATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_SEVERITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
