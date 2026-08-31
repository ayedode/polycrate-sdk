from typing import Literal

UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

UI_K8S_APPS_INSTALL_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_ui_k8s_apps_install_create_pods_status_updated_at_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreatePodsStatusUpdatedAtErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
