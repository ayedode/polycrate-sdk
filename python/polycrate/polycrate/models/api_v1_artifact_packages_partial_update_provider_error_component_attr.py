from typing import Literal

ApiV1ArtifactPackagesPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_artifact_packages_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
