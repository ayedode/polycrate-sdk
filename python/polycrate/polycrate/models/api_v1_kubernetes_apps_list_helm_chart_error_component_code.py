from typing import Literal

ApiV1KubernetesAppsListHelmChartErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_APPS_LIST_HELM_CHART_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsListHelmChartErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_apps_list_helm_chart_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsListHelmChartErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_LIST_HELM_CHART_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_HELM_CHART_ERROR_COMPONENT_CODE_VALUES!r}"
    )
