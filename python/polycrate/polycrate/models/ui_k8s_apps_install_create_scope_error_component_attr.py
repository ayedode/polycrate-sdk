from typing import Literal

UiK8SAppsInstallCreateScopeErrorComponentAttr = Literal["scope"]

UI_K8S_APPS_INSTALL_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[UiK8SAppsInstallCreateScopeErrorComponentAttr] = {
    "scope",
}


def check_ui_k8s_apps_install_create_scope_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateScopeErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
