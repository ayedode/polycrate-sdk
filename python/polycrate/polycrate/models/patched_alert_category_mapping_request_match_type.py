from typing import Literal

PatchedAlertCategoryMappingRequestMatchType = Literal["contains", "contains_all", "exact", "prefix"]

PATCHED_ALERT_CATEGORY_MAPPING_REQUEST_MATCH_TYPE_VALUES: set[PatchedAlertCategoryMappingRequestMatchType] = {
    "contains",
    "contains_all",
    "exact",
    "prefix",
}


def check_patched_alert_category_mapping_request_match_type(value: str) -> PatchedAlertCategoryMappingRequestMatchType:
    if value in PATCHED_ALERT_CATEGORY_MAPPING_REQUEST_MATCH_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ALERT_CATEGORY_MAPPING_REQUEST_MATCH_TYPE_VALUES!r}"
    )
