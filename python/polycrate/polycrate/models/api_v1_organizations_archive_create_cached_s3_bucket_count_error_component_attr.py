from typing import Literal

ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponentAttr = Literal["cached_s3_bucket_count"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_S3_BUCKET_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponentAttr
] = {
    "cached_s3_bucket_count",
}


def check_api_v1_organizations_archive_create_cached_s3_bucket_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_S3_BUCKET_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_S3_BUCKET_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
