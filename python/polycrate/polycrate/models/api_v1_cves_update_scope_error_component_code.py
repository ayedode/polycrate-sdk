from typing import Literal

ApiV1CvesUpdateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CVES_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesUpdateScopeErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_cves_update_scope_error_component_code(value: str) -> ApiV1CvesUpdateScopeErrorComponentCode:
    if value in API_V1_CVES_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
