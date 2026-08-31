from typing import Literal

ApiV1S3BucketsArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1s3_buckets_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1S3BucketsArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
