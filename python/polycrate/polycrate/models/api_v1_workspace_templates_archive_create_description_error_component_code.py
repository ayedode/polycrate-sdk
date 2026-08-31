from typing import Literal

ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspace_templates_archive_create_description_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesArchiveCreateDescriptionErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
