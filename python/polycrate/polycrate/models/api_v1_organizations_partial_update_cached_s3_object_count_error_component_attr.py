from typing import Literal

ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponentAttr = Literal["cached_s3_object_count"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_S3_OBJECT_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponentAttr
] = {
    "cached_s3_object_count",
}


def check_api_v1_organizations_partial_update_cached_s3_object_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_S3_OBJECT_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_S3_OBJECT_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
