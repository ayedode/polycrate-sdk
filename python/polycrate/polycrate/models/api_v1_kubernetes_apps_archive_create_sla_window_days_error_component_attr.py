from typing import Literal

ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_kubernetes_apps_archive_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
