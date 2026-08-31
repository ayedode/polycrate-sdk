from typing import Literal

ApiV1S3BucketsListS3ClusterErrorComponentCode = Literal["invalid_choice"]

API_V1S3_BUCKETS_LIST_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3BucketsListS3ClusterErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1s3_buckets_list_s3_cluster_error_component_code(
    value: str,
) -> ApiV1S3BucketsListS3ClusterErrorComponentCode:
    if value in API_V1S3_BUCKETS_LIST_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
