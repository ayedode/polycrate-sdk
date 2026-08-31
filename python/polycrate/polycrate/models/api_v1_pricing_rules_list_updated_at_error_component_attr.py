from typing import Literal

ApiV1PricingRulesListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_PRICING_RULES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_pricing_rules_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1PricingRulesListUpdatedAtErrorComponentAttr:
    if value in API_V1_PRICING_RULES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
