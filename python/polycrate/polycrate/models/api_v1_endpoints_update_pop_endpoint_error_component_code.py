from typing import Literal

ApiV1EndpointsUpdatePopEndpointErrorComponentCode = Literal["invalid", "null"]

API_V1_ENDPOINTS_UPDATE_POP_ENDPOINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsUpdatePopEndpointErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_endpoints_update_pop_endpoint_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdatePopEndpointErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_POP_ENDPOINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_POP_ENDPOINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
