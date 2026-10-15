from typing import Literal

S3ClusterListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

S3_CLUSTER_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[S3ClusterListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_s3_cluster_list_effective_criticality_type_3_type_1(
    value: str,
) -> S3ClusterListEffectiveCriticalityType3Type1:
    if value in S3_CLUSTER_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {S3_CLUSTER_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
