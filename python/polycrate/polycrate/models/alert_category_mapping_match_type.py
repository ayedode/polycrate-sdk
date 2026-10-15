from typing import Literal

AlertCategoryMappingMatchType = Literal["contains", "contains_all", "exact", "prefix"]

ALERT_CATEGORY_MAPPING_MATCH_TYPE_VALUES: set[AlertCategoryMappingMatchType] = {
    "contains",
    "contains_all",
    "exact",
    "prefix",
}


def check_alert_category_mapping_match_type(value: str) -> AlertCategoryMappingMatchType:
    if value in ALERT_CATEGORY_MAPPING_MATCH_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_MAPPING_MATCH_TYPE_VALUES!r}")
