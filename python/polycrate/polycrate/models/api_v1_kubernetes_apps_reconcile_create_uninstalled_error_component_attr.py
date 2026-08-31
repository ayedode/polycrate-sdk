from typing import Literal

ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponentAttr = Literal["uninstalled"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponentAttr
] = {
    "uninstalled",
}


def check_api_v1_kubernetes_apps_reconcile_create_uninstalled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateUninstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
