from typing import Literal

ApiV1ArtifactsPartialUpdateDigestErrorComponentAttr = Literal["digest"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateDigestErrorComponentAttr
] = {
    "digest",
}


def check_api_v1_artifacts_partial_update_digest_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateDigestErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
