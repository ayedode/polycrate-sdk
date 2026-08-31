from typing import Literal

ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1S3_CLUSTERS_UPDATE_MINIO_CLUSTER_USAGE_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1s3_clusters_update_minio_cluster_usage_bytes_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_MINIO_CLUSTER_USAGE_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_MINIO_CLUSTER_USAGE_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
