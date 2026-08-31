from typing import Literal

UiK8SAppsInstallCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

UI_K8S_APPS_INSTALL_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_ui_k8s_apps_install_create_non_field_errors_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateNonFieldErrorsErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
