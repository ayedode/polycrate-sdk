from typing import Literal

UiK8SAppsInstallCreateHelmChartErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

UI_K8S_APPS_INSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsInstallCreateHelmChartErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_ui_k8s_apps_install_create_helm_chart_error_component_code(
    value: str,
) -> UiK8SAppsInstallCreateHelmChartErrorComponentCode:
    if value in UI_K8S_APPS_INSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_INSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES!r}"
    )
