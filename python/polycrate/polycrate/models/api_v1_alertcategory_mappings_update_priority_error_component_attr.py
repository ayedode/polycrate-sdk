from typing import Literal

ApiV1AlertcategoryMappingsUpdatePriorityErrorComponentAttr = Literal["priority"]

API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsUpdatePriorityErrorComponentAttr
] = {
    "priority",
}


def check_api_v1_alertcategory_mappings_update_priority_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsUpdatePriorityErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_PRIORITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
