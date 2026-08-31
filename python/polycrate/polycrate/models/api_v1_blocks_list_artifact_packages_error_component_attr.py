from typing import Literal

ApiV1BlocksListArtifactPackagesErrorComponentAttr = Literal["artifact_packages"]

API_V1_BLOCKS_LIST_ARTIFACT_PACKAGES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksListArtifactPackagesErrorComponentAttr
] = {
    "artifact_packages",
}


def check_api_v1_blocks_list_artifact_packages_error_component_attr(
    value: str,
) -> ApiV1BlocksListArtifactPackagesErrorComponentAttr:
    if value in API_V1_BLOCKS_LIST_ARTIFACT_PACKAGES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_ARTIFACT_PACKAGES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
