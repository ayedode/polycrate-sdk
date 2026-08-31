from typing import Literal

ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_catalogue_apps_sync_releases_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsSyncReleasesCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_SYNC_RELEASES_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
