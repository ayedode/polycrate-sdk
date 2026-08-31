from typing import Literal

ApiV1ArtifactPackagesCreateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_ARTIFACT_PACKAGES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_artifact_packages_create_kind_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesCreateKindErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
