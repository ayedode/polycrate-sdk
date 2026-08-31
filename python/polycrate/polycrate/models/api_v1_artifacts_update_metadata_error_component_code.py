from typing import Literal

ApiV1ArtifactsUpdateMetadataErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACTS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsUpdateMetadataErrorComponentCode] = {
    "invalid",
}


def check_api_v1_artifacts_update_metadata_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateMetadataErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
