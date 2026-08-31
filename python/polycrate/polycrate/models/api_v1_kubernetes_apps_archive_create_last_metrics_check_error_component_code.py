from typing import Literal

ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_apps_archive_create_last_metrics_check_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateLastMetricsCheckErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
