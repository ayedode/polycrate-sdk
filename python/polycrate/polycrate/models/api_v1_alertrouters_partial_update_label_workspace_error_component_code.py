from typing import Literal

ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponentCode = Literal[
    "blank", "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_WORKSPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alertrouters_partial_update_label_workspace_error_component_code(
    value: str,
) -> ApiV1AlertroutersPartialUpdateLabelWorkspaceErrorComponentCode:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_WORKSPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_WORKSPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
