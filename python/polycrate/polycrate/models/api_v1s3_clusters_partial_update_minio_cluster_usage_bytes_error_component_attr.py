from typing import Literal

ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponentAttr = Literal["minio_cluster_usage_bytes"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_MINIO_CLUSTER_USAGE_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponentAttr
] = {
    "minio_cluster_usage_bytes",
}


def check_api_v1s3_clusters_partial_update_minio_cluster_usage_bytes_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_MINIO_CLUSTER_USAGE_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_MINIO_CLUSTER_USAGE_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
