from typing import Literal

S3ClusterScope = Literal["system", "user"]

S3_CLUSTER_SCOPE_VALUES: set[S3ClusterScope] = {
    "system",
    "user",
}


def check_s3_cluster_scope(value: str) -> S3ClusterScope:
    if value in S3_CLUSTER_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_SCOPE_VALUES!r}")
