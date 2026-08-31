from typing import Literal

ApiV1PricingRulesListScopeErrorComponentAttr = Literal["scope"]

API_V1_PRICING_RULES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingRulesListScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_pricing_rules_list_scope_error_component_attr(
    value: str,
) -> ApiV1PricingRulesListScopeErrorComponentAttr:
    if value in API_V1_PRICING_RULES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
