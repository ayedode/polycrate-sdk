from typing import Literal

ApiV1IncidentsCreateSourceItemIdErrorComponentAttr = Literal["source_item_id"]

API_V1_INCIDENTS_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsCreateSourceItemIdErrorComponentAttr
] = {
    "source_item_id",
}


def check_api_v1_incidents_create_source_item_id_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateSourceItemIdErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_SOURCE_ITEM_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
