from typing import Literal

ApiV1EndpointsPartialUpdateSpecErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsPartialUpdateSpecErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_endpoints_partial_update_spec_error_component_code(
    value: str,
) -> ApiV1EndpointsPartialUpdateSpecErrorComponentCode:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
