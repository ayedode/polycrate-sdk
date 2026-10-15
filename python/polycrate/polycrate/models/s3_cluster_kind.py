from typing import Literal

S3ClusterKind = Literal["minio", "rook-ceph"]

S3_CLUSTER_KIND_VALUES: set[S3ClusterKind] = {
    "minio",
    "rook-ceph",
}


def check_s3_cluster_kind(value: str) -> S3ClusterKind:
    if value in S3_CLUSTER_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_KIND_VALUES!r}")
