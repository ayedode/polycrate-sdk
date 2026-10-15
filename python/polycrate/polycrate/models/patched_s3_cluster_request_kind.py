from typing import Literal

PatchedS3ClusterRequestKind = Literal["minio", "rook-ceph"]

PATCHED_S3_CLUSTER_REQUEST_KIND_VALUES: set[PatchedS3ClusterRequestKind] = {
    "minio",
    "rook-ceph",
}


def check_patched_s3_cluster_request_kind(value: str) -> PatchedS3ClusterRequestKind:
    if value in PATCHED_S3_CLUSTER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_S3_CLUSTER_REQUEST_KIND_VALUES!r}")
