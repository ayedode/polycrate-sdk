from typing import Literal

ApiV1ArtifactRepositoriesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_artifact_repositories_create_provider_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateProviderErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
