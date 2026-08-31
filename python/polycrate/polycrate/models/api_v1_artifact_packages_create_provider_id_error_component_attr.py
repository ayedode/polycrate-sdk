from typing import Literal

ApiV1ArtifactPackagesCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ARTIFACT_PACKAGES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_artifact_packages_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateProviderIdErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
