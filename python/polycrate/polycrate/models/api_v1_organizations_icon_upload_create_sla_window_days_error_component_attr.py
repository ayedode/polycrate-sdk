from typing import Literal

ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_organizations_icon_upload_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
