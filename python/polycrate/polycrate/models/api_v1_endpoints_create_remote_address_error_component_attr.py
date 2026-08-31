from typing import Literal

ApiV1EndpointsCreateRemoteAddressErrorComponentAttr = Literal["remote_address"]

API_V1_ENDPOINTS_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateRemoteAddressErrorComponentAttr
] = {
    "remote_address",
}


def check_api_v1_endpoints_create_remote_address_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateRemoteAddressErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
