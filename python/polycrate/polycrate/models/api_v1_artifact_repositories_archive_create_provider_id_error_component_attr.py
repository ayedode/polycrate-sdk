from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_artifact_repositories_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
