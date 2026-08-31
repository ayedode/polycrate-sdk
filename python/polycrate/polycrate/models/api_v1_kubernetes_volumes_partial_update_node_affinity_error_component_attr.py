from typing import Literal

ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponentAttr = Literal["node_affinity"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_NODE_AFFINITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponentAttr
] = {
    "node_affinity",
}


def check_api_v1_kubernetes_volumes_partial_update_node_affinity_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_NODE_AFFINITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_NODE_AFFINITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
