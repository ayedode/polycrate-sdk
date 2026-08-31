from typing import Literal

ApiV1ArtifactRepositoriesUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_artifact_repositories_update_archived_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateArchivedErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
