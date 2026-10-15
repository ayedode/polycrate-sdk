from typing import Literal

S3ClusterLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

S3_CLUSTER_LAST_STATE_VALUES: set[S3ClusterLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_s3_cluster_last_state(value: str) -> S3ClusterLastState:
    if value in S3_CLUSTER_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_LAST_STATE_VALUES!r}")
