from typing import Literal

ApiV1AlertcategoryMappingsCreatePriorityErrorComponentAttr = Literal["priority"]

API_V1_ALERTCATEGORY_MAPPINGS_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsCreatePriorityErrorComponentAttr
] = {
    "priority",
}


def check_api_v1_alertcategory_mappings_create_priority_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsCreatePriorityErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_CREATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
