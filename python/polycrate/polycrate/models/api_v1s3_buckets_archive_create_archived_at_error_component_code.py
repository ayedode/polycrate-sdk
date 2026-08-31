from typing import Literal

ApiV1S3BucketsArchiveCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsArchiveCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1s3_buckets_archive_create_archived_at_error_component_code(
    value: str,
) -> ApiV1S3BucketsArchiveCreateArchivedAtErrorComponentCode:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
