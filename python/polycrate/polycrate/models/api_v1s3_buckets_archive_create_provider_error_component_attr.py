from typing import Literal

ApiV1S3BucketsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1s3_buckets_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1S3BucketsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
