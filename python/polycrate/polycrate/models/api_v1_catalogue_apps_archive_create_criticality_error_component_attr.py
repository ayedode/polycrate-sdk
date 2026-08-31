from typing import Literal

ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_catalogue_apps_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
