from typing import Literal

S3ClusterRequestCriticalityType1 = Literal["", "high", "low", "medium"]

S3_CLUSTER_REQUEST_CRITICALITY_TYPE_1_VALUES: set[S3ClusterRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_s3_cluster_request_criticality_type_1(value: str) -> S3ClusterRequestCriticalityType1:
    if value in S3_CLUSTER_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
