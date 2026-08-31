from typing import Literal

ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponentAttr = Literal["radosgw_buckets_logical_used_bytes"]

API_V1S3_CLUSTERS_UPDATE_RADOSGW_BUCKETS_LOGICAL_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponentAttr
] = {
    "radosgw_buckets_logical_used_bytes",
}


def check_api_v1s3_clusters_update_radosgw_buckets_logical_used_bytes_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_RADOSGW_BUCKETS_LOGICAL_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_RADOSGW_BUCKETS_LOGICAL_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
