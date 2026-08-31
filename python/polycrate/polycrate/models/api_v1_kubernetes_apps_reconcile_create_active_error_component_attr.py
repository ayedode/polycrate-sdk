from typing import Literal

ApiV1KubernetesAppsReconcileCreateActiveErrorComponentAttr = Literal["active"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_kubernetes_apps_reconcile_create_active_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateActiveErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
