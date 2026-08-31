from typing import Literal

ApiV1PricingRulesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_RULES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_rules_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingRulesCreateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_RULES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
