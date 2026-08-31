from typing import Literal

ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponentAttr = Literal["remote_address"]

API_V1_ENDPOINTS_DISCOVER_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponentAttr
] = {
    "remote_address",
}


def check_api_v1_endpoints_discover_create_remote_address_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
