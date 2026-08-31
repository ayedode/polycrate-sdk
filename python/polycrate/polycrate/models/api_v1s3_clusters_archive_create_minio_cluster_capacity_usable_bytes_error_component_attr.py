from typing import Literal

ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponentAttr = Literal[
    "minio_cluster_capacity_usable_bytes"
]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_MINIO_CLUSTER_CAPACITY_USABLE_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponentAttr
] = {
    "minio_cluster_capacity_usable_bytes",
}


def check_api_v1s3_clusters_archive_create_minio_cluster_capacity_usable_bytes_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_MINIO_CLUSTER_CAPACITY_USABLE_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_MINIO_CLUSTER_CAPACITY_USABLE_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
