from typing import Literal

UiK8SAppsInstallCreateLastInstallationErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

UI_K8S_APPS_INSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateLastInstallationErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_ui_k8s_apps_install_create_last_installation_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateLastInstallationErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
