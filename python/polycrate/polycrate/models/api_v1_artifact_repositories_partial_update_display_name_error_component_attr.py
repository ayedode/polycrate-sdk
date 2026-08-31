from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_artifact_repositories_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
