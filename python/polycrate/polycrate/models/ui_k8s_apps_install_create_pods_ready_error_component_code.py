from typing import Literal

UiK8SAppsInstallCreatePodsReadyErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

UI_K8S_APPS_INSTALL_CREATE_PODS_READY_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreatePodsReadyErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_ui_k8s_apps_install_create_pods_ready_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreatePodsReadyErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_PODS_READY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PODS_READY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
