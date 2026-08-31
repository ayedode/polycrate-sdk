from typing import Literal

ApiV1S3BucketsListS3ClusterErrorComponentAttr = Literal["s3_cluster"]

API_V1S3_BUCKETS_LIST_S3_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3BucketsListS3ClusterErrorComponentAttr] = {
    "s3_cluster",
}


def check_api_v1s3_buckets_list_s3_cluster_error_component_attr(
    value: str,
) -> ApiV1S3BucketsListS3ClusterErrorComponentAttr:
    if value in API_V1S3_BUCKETS_LIST_S3_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_S3_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
