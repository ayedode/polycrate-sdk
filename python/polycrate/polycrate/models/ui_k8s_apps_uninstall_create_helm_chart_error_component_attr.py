from typing import Literal

UiK8SAppsUninstallCreateHelmChartErrorComponentAttr = Literal["helm_chart"]

UI_K8S_APPS_UNINSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES: set[
    UiK8SAppsUninstallCreateHelmChartErrorComponentAttr
] = {
    "helm_chart",
}


def check_ui_k8s_apps_uninstall_create_helm_chart_error_component_attr(
    value: str,
) -> UiK8SAppsUninstallCreateHelmChartErrorComponentAttr:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
