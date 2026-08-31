from typing import Literal

ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponentAttr = Literal[
    "minio_cluster_capacity_usable_bytes"
]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_MINIO_CLUSTER_CAPACITY_USABLE_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponentAttr
] = {
    "minio_cluster_capacity_usable_bytes",
}


def check_api_v1s3_clusters_partial_update_minio_cluster_capacity_usable_bytes_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_MINIO_CLUSTER_CAPACITY_USABLE_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_MINIO_CLUSTER_CAPACITY_USABLE_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
