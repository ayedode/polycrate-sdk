from typing import Literal

S3ClusterRequestKind = Literal["minio", "rook-ceph"]

S3_CLUSTER_REQUEST_KIND_VALUES: set[S3ClusterRequestKind] = {
    "minio",
    "rook-ceph",
}


def check_s3_cluster_request_kind(value: str) -> S3ClusterRequestKind:
    if value in S3_CLUSTER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_REQUEST_KIND_VALUES!r}")
