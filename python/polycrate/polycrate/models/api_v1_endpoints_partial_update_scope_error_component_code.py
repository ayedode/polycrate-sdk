from typing import Literal

ApiV1EndpointsPartialUpdateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsPartialUpdateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_endpoints_partial_update_scope_error_component_code(
    value: str,
) -> ApiV1EndpointsPartialUpdateScopeErrorComponentCode:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
