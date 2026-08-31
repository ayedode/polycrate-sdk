from typing import Literal

ApiV1ArtifactPackagesUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ARTIFACT_PACKAGES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_artifact_packages_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateCriticalityErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
