from typing import Literal

ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponentAttr = Literal["excluded_from_downtime_until"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponentAttr
] = {
    "excluded_from_downtime_until",
}


def check_api_v1_kubernetes_apps_archive_create_excluded_from_downtime_until_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateExcludedFromDowntimeUntilErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_EXCLUDED_FROM_DOWNTIME_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
