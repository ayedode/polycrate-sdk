from typing import Literal

ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponentAttr = Literal["managed_buckets_usage_kb"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponentAttr
] = {
    "managed_buckets_usage_kb",
}


def check_api_v1s3_clusters_partial_update_managed_buckets_usage_kb_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
