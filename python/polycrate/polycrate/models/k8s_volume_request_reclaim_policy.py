from typing import Literal

K8SVolumeRequestReclaimPolicy = Literal["Delete", "Recycle", "Retain"]

K8S_VOLUME_REQUEST_RECLAIM_POLICY_VALUES: set[K8SVolumeRequestReclaimPolicy] = {
    "Delete",
    "Recycle",
    "Retain",
}


def check_k8s_volume_request_reclaim_policy(value: str) -> K8SVolumeRequestReclaimPolicy:
    if value in K8S_VOLUME_REQUEST_RECLAIM_POLICY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_REQUEST_RECLAIM_POLICY_VALUES!r}")
