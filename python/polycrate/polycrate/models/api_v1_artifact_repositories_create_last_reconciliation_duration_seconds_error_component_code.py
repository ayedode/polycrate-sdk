from typing import Literal

ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponentCode = Literal[
    "invalid", "max_string_length"
]

API_V1_ARTIFACT_REPOSITORIES_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
}


def check_api_v1_artifact_repositories_create_last_reconciliation_duration_seconds_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
