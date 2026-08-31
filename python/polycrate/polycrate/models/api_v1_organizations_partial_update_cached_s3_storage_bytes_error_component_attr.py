from typing import Literal

ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponentAttr = Literal["cached_s3_storage_bytes"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_S3_STORAGE_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponentAttr
] = {
    "cached_s3_storage_bytes",
}


def check_api_v1_organizations_partial_update_cached_s3_storage_bytes_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_S3_STORAGE_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_S3_STORAGE_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
