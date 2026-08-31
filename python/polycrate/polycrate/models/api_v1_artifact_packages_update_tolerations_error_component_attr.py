from typing import Literal

ApiV1ArtifactPackagesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ARTIFACT_PACKAGES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_artifact_packages_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
