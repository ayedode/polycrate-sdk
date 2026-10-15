from typing import Literal

S3ClusterState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

S3_CLUSTER_STATE_VALUES: set[S3ClusterState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_s3_cluster_state(value: str) -> S3ClusterState:
    if value in S3_CLUSTER_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_STATE_VALUES!r}")
