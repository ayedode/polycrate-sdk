from typing import Literal

ApiV1EndpointsReconcileCreateRemoteAddressErrorComponentAttr = Literal["remote_address"]

API_V1_ENDPOINTS_RECONCILE_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateRemoteAddressErrorComponentAttr
] = {
    "remote_address",
}


def check_api_v1_endpoints_reconcile_create_remote_address_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateRemoteAddressErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_REMOTE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
