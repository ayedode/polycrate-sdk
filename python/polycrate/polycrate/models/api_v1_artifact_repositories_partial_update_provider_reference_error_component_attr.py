from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_artifact_repositories_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
