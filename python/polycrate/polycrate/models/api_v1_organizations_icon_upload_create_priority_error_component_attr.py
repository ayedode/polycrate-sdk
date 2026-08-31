from typing import Literal

ApiV1OrganizationsIconUploadCreatePriorityErrorComponentAttr = Literal["priority"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreatePriorityErrorComponentAttr
] = {
    "priority",
}


def check_api_v1_organizations_icon_upload_create_priority_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreatePriorityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
