from typing import Literal

ApiV1EndpointsCreateSpecErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_CREATE_SPEC_ERROR_COMPONENT_CODE_VALUES: set[ApiV1EndpointsCreateSpecErrorComponentCode] = {
    "invalid",
}


def check_api_v1_endpoints_create_spec_error_component_code(value: str) -> ApiV1EndpointsCreateSpecErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
