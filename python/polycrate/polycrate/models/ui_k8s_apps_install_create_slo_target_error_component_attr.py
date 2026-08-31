from typing import Literal

UiK8SAppsInstallCreateSloTargetErrorComponentAttr = Literal["slo_target"]

UI_K8S_APPS_INSTALL_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsInstallCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_ui_k8s_apps_install_create_slo_target_error_component_attr(
    value: str,
) -> UiK8SAppsInstallCreateSloTargetErrorComponentAttr:
    if value in UI_K8S_APPS_INSTALL_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
