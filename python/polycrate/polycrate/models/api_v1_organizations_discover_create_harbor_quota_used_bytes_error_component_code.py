from typing import Literal

ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_QUOTA_USED_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_organizations_discover_create_harbor_quota_used_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_QUOTA_USED_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_QUOTA_USED_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
