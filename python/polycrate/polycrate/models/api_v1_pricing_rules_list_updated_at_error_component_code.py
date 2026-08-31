from typing import Literal

ApiV1PricingRulesListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_PRICING_RULES_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesListUpdatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_rules_list_updated_at_error_component_code(
    value: str,
) -> ApiV1PricingRulesListUpdatedAtErrorComponentCode:
    if value in API_V1_PRICING_RULES_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
