from typing import Literal

ApiV1EndpointsUpdateRemoteAddressErrorComponentAttr = Literal["remote_address"]

API_V1_ENDPOINTS_UPDATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsUpdateRemoteAddressErrorComponentAttr
] = {
    "remote_address",
}


def check_api_v1_endpoints_update_remote_address_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateRemoteAddressErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
