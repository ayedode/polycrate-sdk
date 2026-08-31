from typing import Literal

ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_VOLUMES_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_volumes_create_reclaim_policy_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesCreateReclaimPolicyErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
