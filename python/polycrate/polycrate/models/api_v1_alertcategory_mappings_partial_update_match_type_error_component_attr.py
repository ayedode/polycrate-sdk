from typing import Literal

ApiV1AlertcategoryMappingsPartialUpdateMatchTypeErrorComponentAttr = Literal["match_type"]

API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_MATCH_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsPartialUpdateMatchTypeErrorComponentAttr
] = {
    "match_type",
}


def check_api_v1_alertcategory_mappings_partial_update_match_type_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsPartialUpdateMatchTypeErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_MATCH_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_MATCH_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
