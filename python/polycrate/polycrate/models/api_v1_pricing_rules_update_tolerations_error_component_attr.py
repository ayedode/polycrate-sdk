from typing import Literal

ApiV1PricingRulesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_RULES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_rules_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingRulesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_RULES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
