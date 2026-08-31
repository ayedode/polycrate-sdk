from typing import Literal

UiK8SAppsInstallCreateArchivedErrorComponentAttr = Literal["archived"]

UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_ui_k8s_apps_install_create_archived_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateArchivedErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
