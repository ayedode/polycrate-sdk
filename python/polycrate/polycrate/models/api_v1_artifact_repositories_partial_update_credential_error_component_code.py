from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_artifact_repositories_partial_update_credential_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateCredentialErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
