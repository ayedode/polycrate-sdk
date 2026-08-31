from typing import Literal

ApiV1KubernetesAppsUpdatePodsTotalErrorComponentAttr = Literal["pods_total"]

API_V1_KUBERNETES_APPS_UPDATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdatePodsTotalErrorComponentAttr
] = {
    "pods_total",
}


def check_api_v1_kubernetes_apps_update_pods_total_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdatePodsTotalErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
