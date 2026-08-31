from typing import Literal

ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponentAttr = Literal["helm_chart"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponentAttr
] = {
    "helm_chart",
}


def check_api_v1_kubernetes_apps_discover_create_helm_chart_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
