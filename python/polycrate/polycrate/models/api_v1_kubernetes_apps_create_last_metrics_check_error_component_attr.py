from typing import Literal

ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponentAttr = Literal["last_metrics_check"]

API_V1_KUBERNETES_APPS_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponentAttr
] = {
    "last_metrics_check",
}


def check_api_v1_kubernetes_apps_create_last_metrics_check_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateLastMetricsCheckErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_LAST_METRICS_CHECK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
