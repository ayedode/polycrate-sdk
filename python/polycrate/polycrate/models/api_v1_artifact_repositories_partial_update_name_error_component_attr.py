from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_artifact_repositories_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateNameErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
