from typing import Literal

ApiV1ArtifactRepositoriesListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_ARTIFACT_REPOSITORIES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_artifact_repositories_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesListUpdatedAtErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
