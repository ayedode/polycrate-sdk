from typing import Literal

ApiV1ArtifactsPartialUpdateDeprecatedErrorComponentAttr = Literal["deprecated"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_DEPRECATED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateDeprecatedErrorComponentAttr
] = {
    "deprecated",
}


def check_api_v1_artifacts_partial_update_deprecated_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateDeprecatedErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_DEPRECATED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_DEPRECATED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
