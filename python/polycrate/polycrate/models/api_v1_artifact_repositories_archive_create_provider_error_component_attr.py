from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_artifact_repositories_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
