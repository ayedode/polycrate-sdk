from typing import Literal

ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_volumes_archive_create_reclaim_policy_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
