from typing import Literal

ApiV1EndpointsReconcileCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_ENDPOINTS_RECONCILE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_endpoints_reconcile_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
