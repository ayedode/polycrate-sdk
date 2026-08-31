from typing import Literal

UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

UI_K8S_APPS_UNINSTALL_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_ui_k8s_apps_uninstall_create_excluded_from_downtime_until_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateExcludedFromDowntimeUntilErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
