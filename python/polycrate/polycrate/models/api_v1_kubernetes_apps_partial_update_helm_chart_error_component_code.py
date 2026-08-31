from typing import Literal

ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_partial_update_helm_chart_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateHelmChartErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES!r}"
    )
