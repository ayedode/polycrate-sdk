from typing import Literal

ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_organizations_icon_upload_create_harbor_quota_hard_bytes_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_HARBOR_QUOTA_HARD_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
