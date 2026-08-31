from typing import Literal

ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspace_templates_archive_create_description_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
