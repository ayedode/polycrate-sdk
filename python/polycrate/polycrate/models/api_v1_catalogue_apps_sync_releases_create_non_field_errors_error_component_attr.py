from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_catalogue_apps_sync_releases_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
