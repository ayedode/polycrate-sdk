from typing import Literal

UiK8SAppsUninstallCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

UI_K8S_APPS_UNINSTALL_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_ui_k8s_apps_uninstall_create_created_by_component_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateCreatedByComponentErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
