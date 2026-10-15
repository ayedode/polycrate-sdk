from typing import Literal

PatchedS3ClusterRequestScope = Literal["system", "user"]

PATCHED_S3_CLUSTER_REQUEST_SCOPE_VALUES: set[PatchedS3ClusterRequestScope] = {
    "system",
    "user",
}


def check_patched_s3_cluster_request_scope(value: str) -> PatchedS3ClusterRequestScope:
    if value in PATCHED_S3_CLUSTER_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_S3_CLUSTER_REQUEST_SCOPE_VALUES!r}")
