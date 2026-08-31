from typing import Literal

ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponentAttr = Literal["helm_chart"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponentAttr
] = {
    "helm_chart",
}


def check_api_v1_kubernetes_apps_reconcile_create_helm_chart_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateHelmChartErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_HELM_CHART_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
