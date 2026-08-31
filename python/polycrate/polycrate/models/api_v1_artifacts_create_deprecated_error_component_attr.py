from typing import Literal

ApiV1ArtifactsCreateDeprecatedErrorComponentAttr = Literal["deprecated"]

API_V1_ARTIFACTS_CREATE_DEPRECATED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsCreateDeprecatedErrorComponentAttr
] = {
    "deprecated",
}


def check_api_v1_artifacts_create_deprecated_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateDeprecatedErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_DEPRECATED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_DEPRECATED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
