from typing import Literal

UiK8SAppsInstallCreateByoaErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_INSTALL_CREATE_BYOA_ERROR_COMPONENT_CODE_VALUES: set[UiK8SAppsInstallCreateByoaErrorComponentCode] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_install_create_byoa_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateByoaErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_BYOA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_BYOA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
