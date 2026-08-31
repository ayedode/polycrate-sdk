from typing import Literal

ApiV1S3BucketsUpdateCorsAllowAllErrorComponentCode = Literal["invalid", "null"]

API_V1S3_BUCKETS_UPDATE_CORS_ALLOW_ALL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsUpdateCorsAllowAllErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_buckets_update_cors_allow_all_error_component_code(
    value: str,
) -> ApiV1S3BucketsUpdateCorsAllowAllErrorComponentCode:
    if value in API_V1S3_BUCKETS_UPDATE_CORS_ALLOW_ALL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_UPDATE_CORS_ALLOW_ALL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
