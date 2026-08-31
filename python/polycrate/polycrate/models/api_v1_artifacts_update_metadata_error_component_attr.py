from typing import Literal

ApiV1ArtifactsUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_ARTIFACTS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsUpdateMetadataErrorComponentAttr] = {
    "metadata",
}


def check_api_v1_artifacts_update_metadata_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateMetadataErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
