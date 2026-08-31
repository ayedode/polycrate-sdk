from typing import Literal

ApiV1ArtifactRepositoriesListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_ARTIFACT_REPOSITORIES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_artifact_repositories_list_created_at_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesListCreatedAtErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
