from typing import Literal

UiK8SAppsInstallCreateManagedByContentTypeErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

UI_K8S_APPS_INSTALL_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateManagedByContentTypeErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_ui_k8s_apps_install_create_managed_by_content_type_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateManagedByContentTypeErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
