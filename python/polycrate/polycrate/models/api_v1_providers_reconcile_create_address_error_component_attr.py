from typing import Literal

ApiV1ProvidersReconcileCreateAddressErrorComponentAttr = Literal["address"]

API_V1_PROVIDERS_RECONCILE_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateAddressErrorComponentAttr
] = {
    "address",
}


def check_api_v1_providers_reconcile_create_address_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateAddressErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_ADDRESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
