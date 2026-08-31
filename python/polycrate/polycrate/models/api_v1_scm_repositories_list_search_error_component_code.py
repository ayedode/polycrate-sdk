from typing import Literal

ApiV1ScmRepositoriesListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_SCM_REPOSITORIES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesListSearchErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_scm_repositories_list_search_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesListSearchErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
