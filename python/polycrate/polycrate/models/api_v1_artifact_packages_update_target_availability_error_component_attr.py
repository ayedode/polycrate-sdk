from typing import Literal

ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_ARTIFACT_PACKAGES_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_artifact_packages_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
