from typing import Literal

S3ClusterRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

S3_CLUSTER_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[S3ClusterRequestCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_s3_cluster_request_created_by_component_type_1(value: str) -> S3ClusterRequestCreatedByComponentType1:
    if value in S3_CLUSTER_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
