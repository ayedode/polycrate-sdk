from typing import Literal

ApiV1IncidentsPartialUpdateSourceItemIdErrorComponentAttr = Literal["source_item_id"]

API_V1_INCIDENTS_PARTIAL_UPDATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateSourceItemIdErrorComponentAttr
] = {
    "source_item_id",
}


def check_api_v1_incidents_partial_update_source_item_id_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateSourceItemIdErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
