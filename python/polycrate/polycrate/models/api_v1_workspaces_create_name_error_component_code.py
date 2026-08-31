from typing import Literal

ApiV1WorkspacesCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1WorkspacesCreateNameErrorComponentCode] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_create_name_error_component_code(value: str) -> ApiV1WorkspacesCreateNameErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
