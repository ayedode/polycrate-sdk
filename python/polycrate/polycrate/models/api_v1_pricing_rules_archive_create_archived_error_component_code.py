from typing import Literal

ApiV1PricingRulesArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_rules_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1PricingRulesArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
