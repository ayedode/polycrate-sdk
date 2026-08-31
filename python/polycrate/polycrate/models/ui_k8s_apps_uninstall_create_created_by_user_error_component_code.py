from typing import Literal

UiK8SAppsUninstallCreateCreatedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

UI_K8S_APPS_UNINSTALL_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateCreatedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_ui_k8s_apps_uninstall_create_created_by_user_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateCreatedByUserErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
