from typing import Literal

ApiV1S3BucketsArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1s3_buckets_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1S3BucketsArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
