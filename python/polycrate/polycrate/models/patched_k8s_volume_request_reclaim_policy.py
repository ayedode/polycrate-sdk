from typing import Literal

PatchedK8SVolumeRequestReclaimPolicy = Literal["Delete", "Recycle", "Retain"]

PATCHED_K8S_VOLUME_REQUEST_RECLAIM_POLICY_VALUES: set[PatchedK8SVolumeRequestReclaimPolicy] = {
    "Delete",
    "Recycle",
    "Retain",
}


def check_patched_k8s_volume_request_reclaim_policy(value: str) -> PatchedK8SVolumeRequestReclaimPolicy:
    if value in PATCHED_K8S_VOLUME_REQUEST_RECLAIM_POLICY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_VOLUME_REQUEST_RECLAIM_POLICY_VALUES!r}")
