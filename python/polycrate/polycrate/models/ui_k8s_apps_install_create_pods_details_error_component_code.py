from typing import Literal

UiK8SAppsInstallCreatePodsDetailsErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_INSTALL_CREATE_PODS_DETAILS_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreatePodsDetailsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_install_create_pods_details_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreatePodsDetailsErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_PODS_DETAILS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PODS_DETAILS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
