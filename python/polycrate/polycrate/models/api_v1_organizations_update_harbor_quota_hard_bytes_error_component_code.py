from typing import Literal

ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ORGANIZATIONS_UPDATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_organizations_update_harbor_quota_hard_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
