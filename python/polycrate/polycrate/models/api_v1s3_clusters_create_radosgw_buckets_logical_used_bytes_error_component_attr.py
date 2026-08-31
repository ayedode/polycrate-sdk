from typing import Literal

ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponentAttr = Literal["radosgw_buckets_logical_used_bytes"]

API_V1S3_CLUSTERS_CREATE_RADOSGW_BUCKETS_LOGICAL_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponentAttr
] = {
    "radosgw_buckets_logical_used_bytes",
}


def check_api_v1s3_clusters_create_radosgw_buckets_logical_used_bytes_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_RADOSGW_BUCKETS_LOGICAL_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_RADOSGW_BUCKETS_LOGICAL_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
