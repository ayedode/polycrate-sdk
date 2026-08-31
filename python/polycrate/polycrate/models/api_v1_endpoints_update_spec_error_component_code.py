from typing import Literal

ApiV1EndpointsUpdateSpecErrorComponentCode = Literal["invalid"]

API_V1_ENDPOINTS_UPDATE_SPEC_ERROR_COMPONENT_CODE_VALUES: set[ApiV1EndpointsUpdateSpecErrorComponentCode] = {
    "invalid",
}


def check_api_v1_endpoints_update_spec_error_component_code(value: str) -> ApiV1EndpointsUpdateSpecErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
