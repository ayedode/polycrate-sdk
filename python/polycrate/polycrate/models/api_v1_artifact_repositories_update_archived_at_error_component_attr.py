from typing import Literal

ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_artifact_repositories_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
