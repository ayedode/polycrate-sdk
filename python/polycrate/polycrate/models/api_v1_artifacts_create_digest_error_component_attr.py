from typing import Literal

ApiV1ArtifactsCreateDigestErrorComponentAttr = Literal["digest"]

API_V1_ARTIFACTS_CREATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsCreateDigestErrorComponentAttr] = {
    "digest",
}


def check_api_v1_artifacts_create_digest_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateDigestErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
