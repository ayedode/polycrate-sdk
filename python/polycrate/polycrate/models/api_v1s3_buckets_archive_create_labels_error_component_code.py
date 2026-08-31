from typing import Literal

ApiV1S3BucketsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1s3_buckets_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1S3BucketsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
