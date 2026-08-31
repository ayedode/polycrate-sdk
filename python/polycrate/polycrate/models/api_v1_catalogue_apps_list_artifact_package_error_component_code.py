from typing import Literal

ApiV1CatalogueAppsListArtifactPackageErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_CATALOGUE_APPS_LIST_ARTIFACT_PACKAGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsListArtifactPackageErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_catalogue_apps_list_artifact_package_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsListArtifactPackageErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_LIST_ARTIFACT_PACKAGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_LIST_ARTIFACT_PACKAGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
