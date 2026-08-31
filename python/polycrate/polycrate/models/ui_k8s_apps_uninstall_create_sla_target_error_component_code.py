from typing import Literal

UiK8SAppsUninstallCreateSlaTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

UI_K8S_APPS_UNINSTALL_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateSlaTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_ui_k8s_apps_uninstall_create_sla_target_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateSlaTargetErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
