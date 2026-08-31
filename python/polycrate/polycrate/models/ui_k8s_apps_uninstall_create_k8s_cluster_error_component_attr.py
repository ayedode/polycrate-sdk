from typing import Literal

UiK8SAppsUninstallCreateK8SClusterErrorComponentAttr = Literal["k8s_cluster"]

UI_K8S_APPS_UNINSTALL_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateK8SClusterErrorComponentAttr
] = {
    "k8s_cluster",
}


def check_ui_k8s_apps_uninstall_create_k8s_cluster_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateK8SClusterErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
