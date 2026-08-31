from typing import Literal

ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponentAttr = Literal["managed_buckets_usage_kb"]

API_V1S3_CLUSTERS_CREATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponentAttr
] = {
    "managed_buckets_usage_kb",
}


def check_api_v1s3_clusters_create_managed_buckets_usage_kb_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_MANAGED_BUCKETS_USAGE_KB_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
