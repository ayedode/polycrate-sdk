from typing import Literal

ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponentAttr = Literal["cached_s3_object_count"]

API_V1_ORGANIZATIONS_CREATE_CACHED_S3_OBJECT_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponentAttr
] = {
    "cached_s3_object_count",
}


def check_api_v1_organizations_create_cached_s3_object_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_CACHED_S3_OBJECT_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_CACHED_S3_OBJECT_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
