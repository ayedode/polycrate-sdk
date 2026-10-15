from typing import Literal

S3ClusterListKind = Literal["minio", "rook-ceph"]

S3_CLUSTER_LIST_KIND_VALUES: set[S3ClusterListKind] = {
    "minio",
    "rook-ceph",
}


def check_s3_cluster_list_kind(value: str) -> S3ClusterListKind:
    if value in S3_CLUSTER_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_LIST_KIND_VALUES!r}")
