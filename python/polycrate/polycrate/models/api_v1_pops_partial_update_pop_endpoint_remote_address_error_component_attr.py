from typing import Literal

ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponentAttr = Literal["pop_endpoint_remote_address"]

API_V1_POPS_PARTIAL_UPDATE_POP_ENDPOINT_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponentAttr
] = {
    "pop_endpoint_remote_address",
}


def check_api_v1_pops_partial_update_pop_endpoint_remote_address_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_POP_ENDPOINT_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_POP_ENDPOINT_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
