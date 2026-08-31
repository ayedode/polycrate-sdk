from typing import Literal

ApiV1ArtifactsArchiveCreateDigestErrorComponentAttr = Literal["digest"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateDigestErrorComponentAttr
] = {
    "digest",
}


def check_api_v1_artifacts_archive_create_digest_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateDigestErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_DIGEST_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
