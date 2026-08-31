from typing import Literal

ApiV1KubernetesVolumesCreateNodeAffinityErrorComponentAttr = Literal["node_affinity"]

API_V1_KUBERNETES_VOLUMES_CREATE_NODE_AFFINITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateNodeAffinityErrorComponentAttr
] = {
    "node_affinity",
}


def check_api_v1_kubernetes_volumes_create_node_affinity_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateNodeAffinityErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_NODE_AFFINITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_NODE_AFFINITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
