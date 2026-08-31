from typing import Literal

ApiV1AlertsReconcileCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_ALERTS_RECONCILE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_alerts_reconcile_create_namespace_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateNamespaceErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
