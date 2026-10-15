from typing import Literal

S3ClusterRequestScope = Literal["system", "user"]

S3_CLUSTER_REQUEST_SCOPE_VALUES: set[S3ClusterRequestScope] = {
    "system",
    "user",
}


def check_s3_cluster_request_scope(value: str) -> S3ClusterRequestScope:
    if value in S3_CLUSTER_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_REQUEST_SCOPE_VALUES!r}")
