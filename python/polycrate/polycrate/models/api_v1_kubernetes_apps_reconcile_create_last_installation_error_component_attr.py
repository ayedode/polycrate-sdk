from typing import Literal

ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponentAttr = Literal["last_installation"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponentAttr
] = {
    "last_installation",
}


def check_api_v1_kubernetes_apps_reconcile_create_last_installation_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateLastInstallationErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
