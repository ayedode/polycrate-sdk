from typing import Literal

ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponentAttr = Literal["alternative_repository_url"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_ALTERNATIVE_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponentAttr
] = {
    "alternative_repository_url",
}


def check_api_v1_artifact_repositories_update_alternative_repository_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_ALTERNATIVE_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_ALTERNATIVE_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
