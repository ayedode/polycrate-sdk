from typing import Literal

ApiV1KubernetesAppsInstallCreateHelmChartErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsInstallCreateHelmChartErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_install_create_helm_chart_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateHelmChartErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES!r}"
    )
