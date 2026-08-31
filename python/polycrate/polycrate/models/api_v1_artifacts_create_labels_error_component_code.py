from typing import Literal

ApiV1ArtifactsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_artifacts_create_labels_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreateLabelsErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
