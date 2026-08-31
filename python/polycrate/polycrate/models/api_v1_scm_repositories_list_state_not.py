from typing import Literal

ApiV1ScmRepositoriesListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_SCM_REPOSITORIES_LIST_STATE_NOT_VALUES: set[ApiV1ScmRepositoriesListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_scm_repositories_list_state_not(value: str) -> ApiV1ScmRepositoriesListStateNot:
    if value in API_V1_SCM_REPOSITORIES_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_LIST_STATE_NOT_VALUES!r}")
