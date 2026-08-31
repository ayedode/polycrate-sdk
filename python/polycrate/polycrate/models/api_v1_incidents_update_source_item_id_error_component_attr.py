from typing import Literal

ApiV1IncidentsUpdateSourceItemIdErrorComponentAttr = Literal["source_item_id"]

API_V1_INCIDENTS_UPDATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateSourceItemIdErrorComponentAttr
] = {
    "source_item_id",
}


def check_api_v1_incidents_update_source_item_id_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateSourceItemIdErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
