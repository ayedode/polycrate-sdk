from typing import Literal

ApiV1ArtifactPackagesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ARTIFACT_PACKAGES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_artifact_packages_create_kind_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateKindErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
