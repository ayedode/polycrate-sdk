from typing import Literal

ApiV1ArtifactsCreateChangelogErrorComponentAttr = Literal["changelog"]

API_V1_ARTIFACTS_CREATE_CHANGELOG_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsCreateChangelogErrorComponentAttr] = {
    "changelog",
}


def check_api_v1_artifacts_create_changelog_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateChangelogErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_CHANGELOG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_CHANGELOG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
