from typing import Literal

ApiV1WorkspacesReloadCreateReadmeMdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_RELOAD_CREATE_README_MD_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReloadCreateReadmeMdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_reload_create_readme_md_error_component_code(
    value: str,
) -> ApiV1WorkspacesReloadCreateReadmeMdErrorComponentCode:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_README_MD_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_README_MD_ERROR_COMPONENT_CODE_VALUES!r}"
    )
