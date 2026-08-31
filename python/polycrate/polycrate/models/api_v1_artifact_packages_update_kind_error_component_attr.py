from typing import Literal

ApiV1ArtifactPackagesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_ARTIFACT_PACKAGES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_artifact_packages_update_kind_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesUpdateKindErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
