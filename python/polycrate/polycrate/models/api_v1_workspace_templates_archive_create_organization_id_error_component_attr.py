from typing import Literal

ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_workspace_templates_archive_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesArchiveCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
