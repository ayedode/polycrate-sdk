from typing import Literal

UiK8SAppsInstallCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

UI_K8S_APPS_INSTALL_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_ui_k8s_apps_install_create_non_field_errors_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateNonFieldErrorsErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
