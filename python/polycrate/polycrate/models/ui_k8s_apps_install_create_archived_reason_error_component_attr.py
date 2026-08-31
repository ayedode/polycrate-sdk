from typing import Literal

UiK8SAppsInstallCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_ui_k8s_apps_install_create_archived_reason_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateArchivedReasonErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
