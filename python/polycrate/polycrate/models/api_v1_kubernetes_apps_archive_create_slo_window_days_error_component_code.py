from typing import Literal

ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_kubernetes_apps_archive_create_slo_window_days_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateSloWindowDaysErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
