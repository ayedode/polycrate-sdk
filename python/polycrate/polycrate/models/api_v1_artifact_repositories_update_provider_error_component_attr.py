from typing import Literal

ApiV1ArtifactRepositoriesUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_artifact_repositories_update_provider_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateProviderErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
