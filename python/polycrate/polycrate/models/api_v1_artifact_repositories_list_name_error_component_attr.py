from typing import Literal

ApiV1ArtifactRepositoriesListNameErrorComponentAttr = Literal["name"]

API_V1_ARTIFACT_REPOSITORIES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_artifact_repositories_list_name_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesListNameErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
