from typing import Literal

ApiV1AlertcategoryMappingsCreateMatchTypeErrorComponentAttr = Literal["match_type"]

API_V1_ALERTCATEGORY_MAPPINGS_CREATE_MATCH_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsCreateMatchTypeErrorComponentAttr
] = {
    "match_type",
}


def check_api_v1_alertcategory_mappings_create_match_type_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsCreateMatchTypeErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_CREATE_MATCH_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_CREATE_MATCH_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
