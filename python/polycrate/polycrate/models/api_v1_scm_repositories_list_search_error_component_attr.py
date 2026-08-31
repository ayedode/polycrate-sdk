from typing import Literal

ApiV1ScmRepositoriesListSearchErrorComponentAttr = Literal["search"]

API_V1_SCM_REPOSITORIES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_scm_repositories_list_search_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesListSearchErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
