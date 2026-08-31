from typing import Literal

UiK8SAppsInstallCreateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

UI_K8S_APPS_INSTALL_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateCreatedByUserErrorComponentAttr
] = {
    "created_by_user",
}


def check_ui_k8s_apps_install_create_created_by_user_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateCreatedByUserErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
