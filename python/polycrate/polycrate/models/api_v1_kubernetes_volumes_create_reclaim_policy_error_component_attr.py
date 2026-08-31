from typing import Literal

ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponentAttr = Literal["reclaim_policy"]

API_V1_KUBERNETES_VOLUMES_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponentAttr
] = {
    "reclaim_policy",
}


def check_api_v1_kubernetes_volumes_create_reclaim_policy_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
