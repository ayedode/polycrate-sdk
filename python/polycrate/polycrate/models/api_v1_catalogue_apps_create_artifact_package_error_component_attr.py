from typing import Literal

ApiV1CatalogueAppsCreateArtifactPackageErrorComponentAttr = Literal["artifact_package"]

API_V1_CATALOGUE_APPS_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsCreateArtifactPackageErrorComponentAttr
] = {
    "artifact_package",
}


def check_api_v1_catalogue_apps_create_artifact_package_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsCreateArtifactPackageErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
