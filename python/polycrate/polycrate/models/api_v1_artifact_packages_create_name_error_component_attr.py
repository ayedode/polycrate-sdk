from typing import Literal

ApiV1ArtifactPackagesCreateNameErrorComponentAttr = Literal["name"]

API_V1_ARTIFACT_PACKAGES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_artifact_packages_create_name_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesCreateNameErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
