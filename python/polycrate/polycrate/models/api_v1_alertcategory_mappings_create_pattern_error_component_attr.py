from typing import Literal

ApiV1AlertcategoryMappingsCreatePatternErrorComponentAttr = Literal["pattern"]

API_V1_ALERTCATEGORY_MAPPINGS_CREATE_PATTERN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsCreatePatternErrorComponentAttr
] = {
    "pattern",
}


def check_api_v1_alertcategory_mappings_create_pattern_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsCreatePatternErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_CREATE_PATTERN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_CREATE_PATTERN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
