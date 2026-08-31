from typing import Literal

ApiV1EndpointsPartialUpdateRemoteAddressErrorComponentAttr = Literal["remote_address"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateRemoteAddressErrorComponentAttr
] = {
    "remote_address",
}


def check_api_v1_endpoints_partial_update_remote_address_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateRemoteAddressErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
