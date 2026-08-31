from typing import Literal

ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_catalogue_apps_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
