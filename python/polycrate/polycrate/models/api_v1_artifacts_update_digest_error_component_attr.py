from typing import Literal

ApiV1ArtifactsUpdateDigestErrorComponentAttr = Literal["digest"]

API_V1_ARTIFACTS_UPDATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsUpdateDigestErrorComponentAttr] = {
    "digest",
}


def check_api_v1_artifacts_update_digest_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateDigestErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
