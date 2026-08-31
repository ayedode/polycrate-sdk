from typing import Literal

ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_kubernetes_apps_uninstall_create_slo_window_days_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateSloWindowDaysErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
