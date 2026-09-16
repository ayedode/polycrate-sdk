from typing import Literal

ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponentAttr = Literal["maintainer_id"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MAINTAINER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponentAttr
] = {
    "maintainer_id",
}


def check_api_v1_catalogue_apps_archive_create_maintainer_id_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MAINTAINER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MAINTAINER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
