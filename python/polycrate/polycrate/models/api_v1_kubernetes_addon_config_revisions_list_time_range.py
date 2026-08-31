from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_TIME_RANGE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListTimeRange
] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1_kubernetes_addon_config_revisions_list_time_range(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListTimeRange:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_TIME_RANGE_VALUES!r}"
    )
