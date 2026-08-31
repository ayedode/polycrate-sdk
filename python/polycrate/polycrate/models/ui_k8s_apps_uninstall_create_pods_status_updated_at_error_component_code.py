from typing import Literal

UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

UI_K8S_APPS_UNINSTALL_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_ui_k8s_apps_uninstall_create_pods_status_updated_at_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreatePodsStatusUpdatedAtErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
