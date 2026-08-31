from typing import Literal

ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponentAttr = Literal["reclaim_policy"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_RECLAIM_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponentAttr
] = {
    "reclaim_policy",
}


def check_api_v1_kubernetes_volumes_partial_update_reclaim_policy_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateReclaimPolicyErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_RECLAIM_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_RECLAIM_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
