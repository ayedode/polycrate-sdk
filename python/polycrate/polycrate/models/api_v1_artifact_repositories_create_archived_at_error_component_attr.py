from typing import Literal

ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_artifact_repositories_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
