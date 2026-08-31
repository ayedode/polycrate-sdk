from typing import Literal

ApiV1S3BucketsArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1s3_buckets_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1S3BucketsArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
