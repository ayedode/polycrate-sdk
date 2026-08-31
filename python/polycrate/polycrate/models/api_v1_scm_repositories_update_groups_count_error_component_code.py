from typing import Literal

ApiV1ScmRepositoriesUpdateGroupsCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_SCM_REPOSITORIES_UPDATE_GROUPS_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesUpdateGroupsCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_scm_repositories_update_groups_count_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesUpdateGroupsCountErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_GROUPS_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_GROUPS_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
