from typing import Literal

ApiV1KubernetesAppsListHelmChartErrorComponentAttr = Literal["helm_chart"]

API_V1_KUBERNETES_APPS_LIST_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsListHelmChartErrorComponentAttr
] = {
    "helm_chart",
}


def check_api_v1_kubernetes_apps_list_helm_chart_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsListHelmChartErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_LIST_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
