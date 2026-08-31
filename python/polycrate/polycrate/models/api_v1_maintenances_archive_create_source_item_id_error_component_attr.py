from typing import Literal

ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponentAttr = Literal["source_item_id"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponentAttr
] = {
    "source_item_id",
}


def check_api_v1_maintenances_archive_create_source_item_id_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateSourceItemIdErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
