from typing import Literal

ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_ARTIFACT_PACKAGES_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_artifact_packages_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
