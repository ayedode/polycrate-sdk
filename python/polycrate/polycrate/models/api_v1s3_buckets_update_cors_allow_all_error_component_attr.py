from typing import Literal

ApiV1S3BucketsUpdateCorsAllowAllErrorComponentAttr = Literal["cors_allow_all"]

API_V1S3_BUCKETS_UPDATE_CORS_ALLOW_ALL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsUpdateCorsAllowAllErrorComponentAttr
] = {
    "cors_allow_all",
}


def check_api_v1s3_buckets_update_cors_allow_all_error_component_attr(
    value: str,
) -> ApiV1S3BucketsUpdateCorsAllowAllErrorComponentAttr:
    if value in API_V1S3_BUCKETS_UPDATE_CORS_ALLOW_ALL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_UPDATE_CORS_ALLOW_ALL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
