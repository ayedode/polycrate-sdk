from typing import Literal

ApiV1ScmRepositoriesCreateUsersCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_SCM_REPOSITORIES_CREATE_USERS_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesCreateUsersCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_scm_repositories_create_users_count_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesCreateUsersCountErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_CREATE_USERS_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_USERS_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
