from typing import Literal

ApiV1ProvidersReconcileCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PROVIDERS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_providers_reconcile_create_provider_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateProviderErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
