from typing import Literal

ApiV1EndpointsListRemoteAddressErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ENDPOINTS_LIST_REMOTE_ADDRESS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsListRemoteAddressErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_endpoints_list_remote_address_error_component_code(
    value: str,
) -> ApiV1EndpointsListRemoteAddressErrorComponentCode:
    if value in API_V1_ENDPOINTS_LIST_REMOTE_ADDRESS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_REMOTE_ADDRESS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
