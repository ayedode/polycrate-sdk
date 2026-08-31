from typing import Literal

ApiV1ArtifactPackagesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ARTIFACT_PACKAGES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_artifact_packages_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateCriticalityErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
