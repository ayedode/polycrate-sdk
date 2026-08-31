from typing import Literal

UiK8SAppsInstallCreateArchivedByErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateArchivedByErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_ui_k8s_apps_install_create_archived_by_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateArchivedByErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
