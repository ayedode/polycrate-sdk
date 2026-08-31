from typing import Literal

ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_scm_repositories_partial_update_display_name_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
