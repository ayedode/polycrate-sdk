from typing import Literal

ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponentAttr = Literal["cached_s3_bucket_count"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_S3_BUCKET_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponentAttr
] = {
    "cached_s3_bucket_count",
}


def check_api_v1_organizations_reconcile_create_cached_s3_bucket_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_S3_BUCKET_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_S3_BUCKET_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
