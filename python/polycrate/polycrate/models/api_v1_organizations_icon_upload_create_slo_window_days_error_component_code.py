from typing import Literal

ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_organizations_icon_upload_create_slo_window_days_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
