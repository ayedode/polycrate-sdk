from typing import Literal

ApiV1ArtifactsCreateMetadataErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACTS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsCreateMetadataErrorComponentCode] = {
    "invalid",
}


def check_api_v1_artifacts_create_metadata_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreateMetadataErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
