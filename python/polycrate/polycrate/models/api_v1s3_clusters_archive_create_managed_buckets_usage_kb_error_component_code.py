from typing import Literal

ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1s3_clusters_archive_create_managed_buckets_usage_kb_error_component_code(
    value: str,
) -> ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponentCode:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_CODE_VALUES!r}"
    )
