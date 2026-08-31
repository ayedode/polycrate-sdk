from typing import Literal

ApiV1ScmRepositoriesListKindErrorComponentAttr = Literal["kind"]

API_V1_SCM_REPOSITORIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ScmRepositoriesListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_scm_repositories_list_kind_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesListKindErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
