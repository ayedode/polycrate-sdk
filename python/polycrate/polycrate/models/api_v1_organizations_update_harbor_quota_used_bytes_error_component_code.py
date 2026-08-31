from typing import Literal

ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ORGANIZATIONS_UPDATE_HARBOR_QUOTA_USED_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_organizations_update_harbor_quota_used_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_HARBOR_QUOTA_USED_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_HARBOR_QUOTA_USED_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
