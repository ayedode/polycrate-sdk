from typing import Literal

ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponentAttr = Literal["pods_restart_count_total"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_PODS_RESTART_COUNT_TOTAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponentAttr
] = {
    "pods_restart_count_total",
}


def check_api_v1_kubernetes_apps_discover_create_pods_restart_count_total_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreatePodsRestartCountTotalErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_PODS_RESTART_COUNT_TOTAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_PODS_RESTART_COUNT_TOTAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
