from typing import Literal

ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_organizations_partial_update_harbor_quota_hard_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
