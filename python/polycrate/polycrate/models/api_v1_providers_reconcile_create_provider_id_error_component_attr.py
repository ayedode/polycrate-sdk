from typing import Literal

ApiV1ProvidersReconcileCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_PROVIDERS_RECONCILE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_providers_reconcile_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateProviderIdErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
