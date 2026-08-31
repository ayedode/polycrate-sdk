from typing import Literal

ApiV1ArtifactPackagesListKindErrorComponentAttr = Literal["kind"]

API_V1_ARTIFACT_PACKAGES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactPackagesListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_artifact_packages_list_kind_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesListKindErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
