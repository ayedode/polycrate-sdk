from typing import Literal

ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_uninstall_create_helm_chart_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateHelmChartErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES!r}"
    )
