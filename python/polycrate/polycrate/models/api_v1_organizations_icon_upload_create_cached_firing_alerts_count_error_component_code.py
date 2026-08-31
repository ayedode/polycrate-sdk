from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_icon_upload_create_cached_firing_alerts_count_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
