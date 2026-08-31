from typing import Literal

ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponentAttr = Literal["reclaim_policy"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponentAttr
] = {
    "reclaim_policy",
}


def check_api_v1_kubernetes_volumes_archive_create_reclaim_policy_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateReclaimPolicyErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_RECLAIM_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
