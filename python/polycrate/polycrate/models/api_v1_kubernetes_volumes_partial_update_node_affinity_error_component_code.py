from typing import Literal

ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_NODE_AFFINITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_volumes_partial_update_node_affinity_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateNodeAffinityErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_NODE_AFFINITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_NODE_AFFINITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
