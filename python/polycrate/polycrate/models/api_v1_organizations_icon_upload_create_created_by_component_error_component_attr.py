from typing import Literal

ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_organizations_icon_upload_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
