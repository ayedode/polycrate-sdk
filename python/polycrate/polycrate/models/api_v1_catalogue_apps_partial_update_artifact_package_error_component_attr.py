from typing import Literal

ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponentAttr = Literal["artifact_package"]

API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponentAttr
] = {
    "artifact_package",
}


def check_api_v1_catalogue_apps_partial_update_artifact_package_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsPartialUpdateArtifactPackageErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_PARTIAL_UPDATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
