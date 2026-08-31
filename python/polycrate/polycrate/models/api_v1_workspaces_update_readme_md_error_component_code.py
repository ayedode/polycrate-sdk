from typing import Literal

ApiV1WorkspacesUpdateReadmeMdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_UPDATE_README_MD_ERROR_COMPONENT_CODE_VALUES: set[ApiV1WorkspacesUpdateReadmeMdErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_update_readme_md_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateReadmeMdErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_README_MD_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_README_MD_ERROR_COMPONENT_CODE_VALUES!r}"
    )
