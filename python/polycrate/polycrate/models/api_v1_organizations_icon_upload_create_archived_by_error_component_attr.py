from typing import Literal

ApiV1OrganizationsIconUploadCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_organizations_icon_upload_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateArchivedByErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
