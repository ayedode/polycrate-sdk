from typing import Literal

ApiV1RegionsPartialUpdateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_REGIONS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsPartialUpdateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_regions_partial_update_scope_error_component_code(
    value: str,
) -> ApiV1RegionsPartialUpdateScopeErrorComponentCode:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
