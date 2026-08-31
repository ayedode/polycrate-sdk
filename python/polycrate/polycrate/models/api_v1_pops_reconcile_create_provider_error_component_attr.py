from typing import Literal

ApiV1PopsReconcileCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_POPS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsReconcileCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pops_reconcile_create_provider_error_component_attr(
    value: str,
) -> ApiV1PopsReconcileCreateProviderErrorComponentAttr:
    if value in API_V1_POPS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
