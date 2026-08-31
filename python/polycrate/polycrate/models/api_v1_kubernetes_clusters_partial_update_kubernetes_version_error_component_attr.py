from typing import Literal

ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponentAttr = Literal["kubernetes_version"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_KUBERNETES_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponentAttr
] = {
    "kubernetes_version",
}


def check_api_v1_kubernetes_clusters_partial_update_kubernetes_version_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateKubernetesVersionErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_KUBERNETES_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_KUBERNETES_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
