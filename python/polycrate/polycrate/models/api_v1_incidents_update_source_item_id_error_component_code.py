from typing import Literal

ApiV1IncidentsUpdateSourceItemIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_INCIDENTS_UPDATE_SOURCE_ITEM_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsUpdateSourceItemIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_incidents_update_source_item_id_error_component_code(
    value: str,
) -> ApiV1IncidentsUpdateSourceItemIdErrorComponentCode:
    if value in API_V1_INCIDENTS_UPDATE_SOURCE_ITEM_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_SOURCE_ITEM_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
