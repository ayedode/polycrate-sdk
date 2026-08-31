from typing import Literal

ApiV1KubernetesVolumesListK8SClusterErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_KUBERNETES_VOLUMES_LIST_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesListK8SClusterErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_list_k8s_cluster_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesListK8SClusterErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
