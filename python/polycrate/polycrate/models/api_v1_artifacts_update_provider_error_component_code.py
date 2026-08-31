from typing import Literal

ApiV1ArtifactsUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ARTIFACTS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsUpdateProviderErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_artifacts_update_provider_error_component_code(
    value: str,
) -> ApiV1ArtifactsUpdateProviderErrorComponentCode:
    if value in API_V1_ARTIFACTS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
