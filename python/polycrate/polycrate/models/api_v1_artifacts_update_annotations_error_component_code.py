from typing import Literal

ApiV1ArtifactsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifacts_update_annotations_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
