from typing import Literal

ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifact_packages_partial_update_provider_reference_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesPartialUpdateProviderReferenceErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
