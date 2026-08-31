from typing import Literal

ApiV1ArtifactRepositoriesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_artifact_repositories_create_archived_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateArchivedErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
