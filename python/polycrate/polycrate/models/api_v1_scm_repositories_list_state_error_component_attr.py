from typing import Literal

ApiV1ScmRepositoriesListStateErrorComponentAttr = Literal["state"]

API_V1_SCM_REPOSITORIES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ScmRepositoriesListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_scm_repositories_list_state_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesListStateErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
