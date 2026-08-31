from typing import Literal

UiK8SAppsUninstallCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

UI_K8S_APPS_UNINSTALL_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_ui_k8s_apps_uninstall_create_archived_at_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateArchivedAtErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
