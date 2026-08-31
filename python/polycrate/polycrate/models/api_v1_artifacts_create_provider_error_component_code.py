from typing import Literal

ApiV1ArtifactsCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ARTIFACTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ArtifactsCreateProviderErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_artifacts_create_provider_error_component_code(
    value: str,
) -> ApiV1ArtifactsCreateProviderErrorComponentCode:
    if value in API_V1_ARTIFACTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
