from typing import Literal

ApiV1EndpointsReconcileCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ENDPOINTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_endpoints_reconcile_create_provider_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateProviderErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
