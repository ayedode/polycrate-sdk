from typing import Literal

ApiV1KubernetesAppsCreateHelmChartErrorComponentAttr = Literal["helm_chart"]

API_V1_KUBERNETES_APPS_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateHelmChartErrorComponentAttr
] = {
    "helm_chart",
}


def check_api_v1_kubernetes_apps_create_helm_chart_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateHelmChartErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
