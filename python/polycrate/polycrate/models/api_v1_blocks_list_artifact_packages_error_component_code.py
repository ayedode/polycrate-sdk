from typing import Literal

ApiV1BlocksListArtifactPackagesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_BLOCKS_LIST_ARTIFACT_PACKAGES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksListArtifactPackagesErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_blocks_list_artifact_packages_error_component_code(
    value: str,
) -> ApiV1BlocksListArtifactPackagesErrorComponentCode:
    if value in API_V1_BLOCKS_LIST_ARTIFACT_PACKAGES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_ARTIFACT_PACKAGES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
