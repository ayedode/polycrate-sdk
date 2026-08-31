from typing import Literal

ApiV1ArtifactsPartialUpdateMetadataErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsPartialUpdateMetadataErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifacts_partial_update_metadata_error_component_code(
    value: str,
) -> ApiV1ArtifactsPartialUpdateMetadataErrorComponentCode:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
