from typing import Literal

ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponentCode = Literal[
    "invalid", "max_string_length"
]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
}


def check_api_v1_artifact_repositories_update_last_reconciliation_duration_seconds_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
