from typing import Literal

K8SVolumeReclaimPolicy = Literal["Delete", "Recycle", "Retain"]

K8S_VOLUME_RECLAIM_POLICY_VALUES: set[K8SVolumeReclaimPolicy] = {
    "Delete",
    "Recycle",
    "Retain",
}


def check_k8s_volume_reclaim_policy(value: str) -> K8SVolumeReclaimPolicy:
    if value in K8S_VOLUME_RECLAIM_POLICY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_RECLAIM_POLICY_VALUES!r}")
