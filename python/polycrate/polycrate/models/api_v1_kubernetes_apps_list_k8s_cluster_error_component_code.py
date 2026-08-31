from typing import Literal

ApiV1KubernetesAppsListK8SClusterErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_APPS_LIST_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsListK8SClusterErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_apps_list_k8s_cluster_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsListK8SClusterErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_LIST_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
