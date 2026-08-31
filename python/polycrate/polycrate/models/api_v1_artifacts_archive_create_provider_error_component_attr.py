from typing import Literal

ApiV1ArtifactsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_artifacts_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
