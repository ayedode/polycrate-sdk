from typing import Literal

ApiV1S3BucketsPartialUpdateCorsAllowAllErrorComponentCode = Literal["invalid", "null"]

API_V1S3_BUCKETS_PARTIAL_UPDATE_CORS_ALLOW_ALL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsPartialUpdateCorsAllowAllErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_buckets_partial_update_cors_allow_all_error_component_code(
    value: str,
) -> ApiV1S3BucketsPartialUpdateCorsAllowAllErrorComponentCode:
    if value in API_V1S3_BUCKETS_PARTIAL_UPDATE_CORS_ALLOW_ALL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_PARTIAL_UPDATE_CORS_ALLOW_ALL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
