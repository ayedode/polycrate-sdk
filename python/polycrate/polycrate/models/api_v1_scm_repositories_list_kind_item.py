from typing import Literal

ApiV1ScmRepositoriesListKindItem = Literal["forgejo", "generic", "gitea", "gitlab"]

API_V1_SCM_REPOSITORIES_LIST_KIND_ITEM_VALUES: set[ApiV1ScmRepositoriesListKindItem] = {
    "forgejo",
    "generic",
    "gitea",
    "gitlab",
}


def check_api_v1_scm_repositories_list_kind_item(value: str) -> ApiV1ScmRepositoriesListKindItem:
    if value in API_V1_SCM_REPOSITORIES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_KIND_ITEM_VALUES!r}")
