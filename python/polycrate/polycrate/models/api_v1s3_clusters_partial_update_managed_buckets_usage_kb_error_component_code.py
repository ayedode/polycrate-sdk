from typing import Literal

ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1s3_clusters_partial_update_managed_buckets_usage_kb_error_component_code(
    value: str,
) -> ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponentCode:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_CODE_VALUES!r}"
    )
