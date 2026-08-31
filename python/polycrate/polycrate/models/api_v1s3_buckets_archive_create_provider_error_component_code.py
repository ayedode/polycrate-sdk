from typing import Literal

ApiV1S3BucketsArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1s3_buckets_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1S3BucketsArchiveCreateProviderErrorComponentCode:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
