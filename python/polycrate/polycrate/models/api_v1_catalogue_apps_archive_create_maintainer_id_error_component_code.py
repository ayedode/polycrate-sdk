from typing import Literal

ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MAINTAINER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_catalogue_apps_archive_create_maintainer_id_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateMaintainerIdErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MAINTAINER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_MAINTAINER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
