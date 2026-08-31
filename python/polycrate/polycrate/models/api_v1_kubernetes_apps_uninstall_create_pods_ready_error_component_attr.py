from typing import Literal

ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponentAttr = Literal["pods_ready"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponentAttr
] = {
    "pods_ready",
}


def check_api_v1_kubernetes_apps_uninstall_create_pods_ready_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreatePodsReadyErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
