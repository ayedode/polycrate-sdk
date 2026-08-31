from typing import Literal

ApiV1ArtifactRepositoriesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ARTIFACT_REPOSITORIES_LIST_STATE_VALUES: set[ApiV1ArtifactRepositoriesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_artifact_repositories_list_state(value: str) -> ApiV1ArtifactRepositoriesListState:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_STATE_VALUES!r}")
