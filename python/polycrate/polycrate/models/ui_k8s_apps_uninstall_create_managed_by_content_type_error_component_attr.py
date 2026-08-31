from typing import Literal

UiK8SAppsUninstallCreateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

UI_K8S_APPS_UNINSTALL_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_ui_k8s_apps_uninstall_create_managed_by_content_type_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateManagedByContentTypeErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
