from typing import Literal

ApiV1PricingRulesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_RULES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingRulesCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_pricing_rules_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingRulesCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_RULES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
