from typing import Literal

ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_artifact_packages_partial_update_created_by_component_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesPartialUpdateCreatedByComponentErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
