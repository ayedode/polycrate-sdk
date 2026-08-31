from typing import Literal

ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_S3_STORAGE_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_partial_update_cached_s3_storage_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_S3_STORAGE_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_S3_STORAGE_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
