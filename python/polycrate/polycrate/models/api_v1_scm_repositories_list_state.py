from typing import Literal

ApiV1ScmRepositoriesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_SCM_REPOSITORIES_LIST_STATE_VALUES: set[ApiV1ScmRepositoriesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_scm_repositories_list_state(value: str) -> ApiV1ScmRepositoriesListState:
    if value in API_V1_SCM_REPOSITORIES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_STATE_VALUES!r}")
