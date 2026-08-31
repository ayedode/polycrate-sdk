from typing import Literal

ApiV1AlertsReconcileCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_ALERTS_RECONCILE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_alerts_reconcile_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
