from typing import Literal

ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponentAttr = Literal["match_type"]

API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_MATCH_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponentAttr
] = {
    "match_type",
}


def check_api_v1_alertcategory_mappings_update_match_type_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsUpdateMatchTypeErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_MATCH_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_MATCH_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
