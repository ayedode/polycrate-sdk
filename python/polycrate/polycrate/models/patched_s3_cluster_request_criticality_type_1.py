from typing import Literal

PatchedS3ClusterRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_S3_CLUSTER_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedS3ClusterRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_s3_cluster_request_criticality_type_1(value: str) -> PatchedS3ClusterRequestCriticalityType1:
    if value in PATCHED_S3_CLUSTER_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_S3_CLUSTER_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
