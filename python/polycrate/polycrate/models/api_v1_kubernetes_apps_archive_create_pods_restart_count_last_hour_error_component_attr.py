from typing import Literal

ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponentAttr = Literal["pods_restart_count_last_hour"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_RESTART_COUNT_LAST_HOUR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponentAttr
] = {
    "pods_restart_count_last_hour",
}


def check_api_v1_kubernetes_apps_archive_create_pods_restart_count_last_hour_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreatePodsRestartCountLastHourErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_RESTART_COUNT_LAST_HOUR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_RESTART_COUNT_LAST_HOUR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
