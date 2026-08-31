from typing import Literal

ApiV1ArtifactRepositoriesCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_artifact_repositories_create_credential_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateCredentialErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
