from typing import Literal

ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponentAttr = Literal["pods_total"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponentAttr
] = {
    "pods_total",
}


def check_api_v1_kubernetes_apps_uninstall_create_pods_total_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreatePodsTotalErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
