from typing import Literal

ApiV1PricingRulesArchiveCreateActiveFromErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesArchiveCreateActiveFromErrorComponentCode
] = {
    "datetime",
    "invalid",
}


def check_api_v1_pricing_rules_archive_create_active_from_error_component_code(
    value: str,
) -> ApiV1PricingRulesArchiveCreateActiveFromErrorComponentCode:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
