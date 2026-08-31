from typing import Literal

ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1_ARTIFACT_PACKAGES_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1_artifact_packages_update_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
