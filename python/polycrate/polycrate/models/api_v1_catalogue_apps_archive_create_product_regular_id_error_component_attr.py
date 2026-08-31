from typing import Literal

ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponentAttr = Literal["product_regular_id"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponentAttr
] = {
    "product_regular_id",
}


def check_api_v1_catalogue_apps_archive_create_product_regular_id_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateProductRegularIdErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_PRODUCT_REGULAR_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
