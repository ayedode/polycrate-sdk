from typing import Literal

UiK8SAppsUninstallCreateArchivedByErrorComponentAttr = Literal["archived_by"]

UI_K8S_APPS_UNINSTALL_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_ui_k8s_apps_uninstall_create_archived_by_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateArchivedByErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
