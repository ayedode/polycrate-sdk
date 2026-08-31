from typing import Literal

ApiV1ArtifactsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ARTIFACTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsCreateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_artifacts_create_provider_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateProviderErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
