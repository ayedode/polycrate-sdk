from typing import Literal

ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_artifact_repositories_update_display_name_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
