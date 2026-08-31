from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_catalogue_apps_sync_releases_create_product_regular_id_error_component_code(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateProductRegularIdErrorComponentCode:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
