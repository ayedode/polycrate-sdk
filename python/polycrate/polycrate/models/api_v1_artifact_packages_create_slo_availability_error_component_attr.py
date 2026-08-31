from typing import Literal

ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_ARTIFACT_PACKAGES_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_artifact_packages_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
