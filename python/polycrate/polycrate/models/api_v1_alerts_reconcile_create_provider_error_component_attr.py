from typing import Literal

ApiV1AlertsReconcileCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_alerts_reconcile_create_provider_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateProviderErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
