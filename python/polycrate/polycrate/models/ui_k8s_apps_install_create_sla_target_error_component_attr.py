from typing import Literal

UiK8SAppsInstallCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

UI_K8S_APPS_INSTALL_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_ui_k8s_apps_install_create_sla_target_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateSlaTargetErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
