from typing import Literal

ApiV1PricingRulesPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_RULES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_rules_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1PricingRulesPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_PRICING_RULES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
