from typing import Literal

ApiV1KubernetesClustersListKubernetesVersionErrorComponentAttr = Literal["kubernetes_version"]

API_V1_KUBERNETES_CLUSTERS_LIST_KUBERNETES_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersListKubernetesVersionErrorComponentAttr
] = {
    "kubernetes_version",
}


def check_api_v1_kubernetes_clusters_list_kubernetes_version_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersListKubernetesVersionErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_KUBERNETES_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_KUBERNETES_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
