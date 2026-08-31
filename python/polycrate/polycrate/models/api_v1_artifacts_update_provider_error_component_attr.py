from typing import Literal

ApiV1ArtifactsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_ARTIFACTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsUpdateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_artifacts_update_provider_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateProviderErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
