from typing import Literal

ApiV1IncidentsArchiveCreateSourceItemIdErrorComponentAttr = Literal["source_item_id"]

API_V1_INCIDENTS_ARCHIVE_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateSourceItemIdErrorComponentAttr
] = {
    "source_item_id",
}


def check_api_v1_incidents_archive_create_source_item_id_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateSourceItemIdErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
