from typing import Literal

ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponentAttr = Literal["repository_url"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponentAttr
] = {
    "repository_url",
}


def check_api_v1_artifact_repositories_create_repository_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
