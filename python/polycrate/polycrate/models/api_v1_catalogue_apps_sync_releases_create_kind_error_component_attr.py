from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_catalogue_apps_sync_releases_create_kind_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateKindErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
