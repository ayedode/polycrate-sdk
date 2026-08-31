from typing import Literal

ApiV1S3BucketsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1s3_buckets_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1S3BucketsArchiveCreateKindErrorComponentAttr:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
