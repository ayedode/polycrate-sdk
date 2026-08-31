from typing import Literal

ApiV1ArtifactsUpdateDeprecatedErrorComponentAttr = Literal["deprecated"]

API_V1_ARTIFACTS_UPDATE_DEPRECATED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateDeprecatedErrorComponentAttr
] = {
    "deprecated",
}


def check_api_v1_artifacts_update_deprecated_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateDeprecatedErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_DEPRECATED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_DEPRECATED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
