from typing import Literal

ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponentAttr = Literal["cached_s3_bucket_count"]

API_V1_ORGANIZATIONS_UPDATE_CACHED_S3_BUCKET_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponentAttr
] = {
    "cached_s3_bucket_count",
}


def check_api_v1_organizations_update_cached_s3_bucket_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_S3_BUCKET_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_S3_BUCKET_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
