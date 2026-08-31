from typing import Literal

ApiV1S3BucketsArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_buckets_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1S3BucketsArchiveCreateArchivedErrorComponentCode:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
