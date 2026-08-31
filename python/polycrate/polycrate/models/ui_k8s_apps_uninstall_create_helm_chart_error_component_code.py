from typing import Literal

UiK8SAppsUninstallCreateHelmChartErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

UI_K8S_APPS_UNINSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateHelmChartErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_ui_k8s_apps_uninstall_create_helm_chart_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateHelmChartErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_CODE_VALUES!r}"
    )
