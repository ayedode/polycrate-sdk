from typing import Literal

ApiV1OrganizationsIconUploadCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_organizations_icon_upload_create_kind_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateKindErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
