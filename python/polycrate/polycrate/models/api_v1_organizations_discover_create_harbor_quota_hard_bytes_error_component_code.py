from typing import Literal

ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_organizations_discover_create_harbor_quota_hard_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
