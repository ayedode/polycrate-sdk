from typing import Literal

ApiV1ScmRepositoriesListNameExactErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_SCM_REPOSITORIES_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesListNameExactErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_scm_repositories_list_name_exact_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesListNameExactErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
