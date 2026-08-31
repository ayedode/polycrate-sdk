from typing import Literal

ApiV1AlertcategoryMappingsListMatchType = Literal["contains", "contains_all", "exact", "prefix"]

API_V1_ALERTCATEGORY_MAPPINGS_LIST_MATCH_TYPE_VALUES: set[ApiV1AlertcategoryMappingsListMatchType] = {
    "contains",
    "contains_all",
    "exact",
    "prefix",
}


def check_api_v1_alertcategory_mappings_list_match_type(value: str) -> ApiV1AlertcategoryMappingsListMatchType:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_LIST_MATCH_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_LIST_MATCH_TYPE_VALUES!r}"
    )
