from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_artifact_repositories_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
