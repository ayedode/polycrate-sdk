from typing import Literal

ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponentAttr = Literal["loopback_org_id"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_LOOPBACK_ORG_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponentAttr
] = {
    "loopback_org_id",
}


def check_api_v1_organizations_icon_upload_create_loopback_org_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_LOOPBACK_ORG_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_LOOPBACK_ORG_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
