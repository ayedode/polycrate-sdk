from typing import Literal

S3ClusterKindEnum = Literal["minio", "rook-ceph"]

S3_CLUSTER_KIND_ENUM_VALUES: set[S3ClusterKindEnum] = {
    "minio",
    "rook-ceph",
}


def check_s3_cluster_kind_enum(value: str) -> S3ClusterKindEnum:
    if value in S3_CLUSTER_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_KIND_ENUM_VALUES!r}")
