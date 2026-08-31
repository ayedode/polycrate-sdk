from typing import Literal

UiK8SAppsInstallCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_ui_k8s_apps_install_create_archived_at_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateArchivedAtErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
