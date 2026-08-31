from typing import Literal

ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponentAttr = Literal["managed_buckets_object_count"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_MANAGED_BUCKETS_OBJECT_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponentAttr
] = {
    "managed_buckets_object_count",
}


def check_api_v1s3_clusters_archive_create_managed_buckets_object_count_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_MANAGED_BUCKETS_OBJECT_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_MANAGED_BUCKETS_OBJECT_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
