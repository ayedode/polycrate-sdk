from typing import Literal

ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponentAttr = Literal["loopback_org_id"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_LOOPBACK_ORG_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponentAttr
] = {
    "loopback_org_id",
}


def check_api_v1_organizations_archive_create_loopback_org_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_LOOPBACK_ORG_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_LOOPBACK_ORG_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
