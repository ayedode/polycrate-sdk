from typing import Literal

UiK8SAppsUninstallCreateArchivedErrorComponentAttr = Literal["archived"]

UI_K8S_APPS_UNINSTALL_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_ui_k8s_apps_uninstall_create_archived_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateArchivedErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
