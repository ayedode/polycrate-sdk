from typing import Literal

ApiV1PopsReconcileCreatePopEndpointRemoteAddressErrorComponentAttr = Literal["pop_endpoint_remote_address"]

API_V1_POPS_RECONCILE_CREATE_POP_ENDPOINT_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsReconcileCreatePopEndpointRemoteAddressErrorComponentAttr
] = {
    "pop_endpoint_remote_address",
}


def check_api_v1_pops_reconcile_create_pop_endpoint_remote_address_error_component_attr(
    value: str,
) -> ApiV1PopsReconcileCreatePopEndpointRemoteAddressErrorComponentAttr:
    if value in API_V1_POPS_RECONCILE_CREATE_POP_ENDPOINT_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_POP_ENDPOINT_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
