from typing import Literal

ApiV1ArtifactPackagesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ARTIFACT_PACKAGES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_artifact_packages_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateTolerationsErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
