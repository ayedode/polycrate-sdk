from typing import Literal

ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACE_TEMPLATES_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspace_templates_update_description_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesUpdateDescriptionErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
