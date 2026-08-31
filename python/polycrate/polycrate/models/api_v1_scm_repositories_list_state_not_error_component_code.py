from typing import Literal

ApiV1ScmRepositoriesListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1_SCM_REPOSITORIES_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesListStateNotErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_scm_repositories_list_state_not_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesListStateNotErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
