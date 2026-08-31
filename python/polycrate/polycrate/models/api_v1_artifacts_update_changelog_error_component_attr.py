from typing import Literal

ApiV1ArtifactsUpdateChangelogErrorComponentAttr = Literal["changelog"]

API_V1_ARTIFACTS_UPDATE_CHANGELOG_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsUpdateChangelogErrorComponentAttr] = {
    "changelog",
}


def check_api_v1_artifacts_update_changelog_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateChangelogErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_CHANGELOG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_CHANGELOG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
