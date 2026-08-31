from typing import Literal

ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_artifact_repositories_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
