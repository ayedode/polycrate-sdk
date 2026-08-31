from typing import Literal

UiK8SAppsUninstallCreateActualAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

UI_K8S_APPS_UNINSTALL_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateActualAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_ui_k8s_apps_uninstall_create_actual_availability_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateActualAvailabilityErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
