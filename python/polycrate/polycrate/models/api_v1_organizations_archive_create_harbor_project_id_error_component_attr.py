from typing import Literal

ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponentAttr = Literal["harbor_project_id"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_HARBOR_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponentAttr
] = {
    "harbor_project_id",
}


def check_api_v1_organizations_archive_create_harbor_project_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_HARBOR_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_HARBOR_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
