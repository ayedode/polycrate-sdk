from typing import Literal

ApiV1KubernetesAppsReconcileCreateInstalledErrorComponentAttr = Literal["installed"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateInstalledErrorComponentAttr
] = {
    "installed",
}


def check_api_v1_kubernetes_apps_reconcile_create_installed_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateInstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
