from typing import Literal

ApiV1S3ClustersUpdateAllowNewBucketsErrorComponentAttr = Literal["allow_new_buckets"]

API_V1S3_CLUSTERS_UPDATE_ALLOW_NEW_BUCKETS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateAllowNewBucketsErrorComponentAttr
] = {
    "allow_new_buckets",
}


def check_api_v1s3_clusters_update_allow_new_buckets_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateAllowNewBucketsErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_ALLOW_NEW_BUCKETS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_ALLOW_NEW_BUCKETS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
