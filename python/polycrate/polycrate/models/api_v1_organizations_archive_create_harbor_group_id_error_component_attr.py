from typing import Literal

ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponentAttr = Literal["harbor_group_id"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponentAttr
] = {
    "harbor_group_id",
}


def check_api_v1_organizations_archive_create_harbor_group_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
