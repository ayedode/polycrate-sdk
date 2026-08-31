from typing import Literal

UiK8SAppsUninstallCreateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

UI_K8S_APPS_UNINSTALL_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_ui_k8s_apps_uninstall_create_managed_by_object_id_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateManagedByObjectIdErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
