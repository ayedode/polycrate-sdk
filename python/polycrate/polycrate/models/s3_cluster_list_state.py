from typing import Literal

S3ClusterListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

S3_CLUSTER_LIST_STATE_VALUES: set[S3ClusterListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_s3_cluster_list_state(value: str) -> S3ClusterListState:
    if value in S3_CLUSTER_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_LIST_STATE_VALUES!r}")
