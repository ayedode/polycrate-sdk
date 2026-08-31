from typing import Literal

ApiV1ScmRepositoriesListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_SCM_REPOSITORIES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_scm_repositories_list_state_not_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesListStateNotErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
