from typing import Literal

ApiV1S3BucketsArchiveCreateCorsAllowAllErrorComponentCode = Literal["invalid", "null"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_CORS_ALLOW_ALL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsArchiveCreateCorsAllowAllErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_buckets_archive_create_cors_allow_all_error_component_code(
    value: str,
) -> ApiV1S3BucketsArchiveCreateCorsAllowAllErrorComponentCode:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_CORS_ALLOW_ALL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_CORS_ALLOW_ALL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
