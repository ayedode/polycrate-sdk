from typing import Literal

ApiV1ContactgroupsArchiveCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_CONTACTGROUPS_ARCHIVE_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsArchiveCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_contactgroups_archive_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsArchiveCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_ARCHIVE_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_ARCHIVE_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
