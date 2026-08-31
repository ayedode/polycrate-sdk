from typing import Literal

ApiV1S3BucketsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1s3_buckets_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1S3BucketsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
