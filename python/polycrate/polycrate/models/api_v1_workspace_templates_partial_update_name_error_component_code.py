from typing import Literal

ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed", "unique"
]

API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_workspace_templates_partial_update_name_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesPartialUpdateNameErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
