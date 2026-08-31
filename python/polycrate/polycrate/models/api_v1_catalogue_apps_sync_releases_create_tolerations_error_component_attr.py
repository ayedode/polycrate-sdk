from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_catalogue_apps_sync_releases_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateTolerationsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
