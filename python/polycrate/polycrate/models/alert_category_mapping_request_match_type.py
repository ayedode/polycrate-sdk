from typing import Literal

AlertCategoryMappingRequestMatchType = Literal["contains", "contains_all", "exact", "prefix"]

ALERT_CATEGORY_MAPPING_REQUEST_MATCH_TYPE_VALUES: set[AlertCategoryMappingRequestMatchType] = {
    "contains",
    "contains_all",
    "exact",
    "prefix",
}


def check_alert_category_mapping_request_match_type(value: str) -> AlertCategoryMappingRequestMatchType:
    if value in ALERT_CATEGORY_MAPPING_REQUEST_MATCH_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_CATEGORY_MAPPING_REQUEST_MATCH_TYPE_VALUES!r}")
