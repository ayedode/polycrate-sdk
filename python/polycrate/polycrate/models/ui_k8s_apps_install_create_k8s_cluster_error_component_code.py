from typing import Literal

UiK8SAppsInstallCreateK8SClusterErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

UI_K8S_APPS_INSTALL_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateK8SClusterErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_ui_k8s_apps_install_create_k8s_cluster_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateK8SClusterErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
