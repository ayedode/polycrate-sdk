from typing import Literal

ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_discover_create_helm_chart_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateHelmChartErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES!r}"
    )
