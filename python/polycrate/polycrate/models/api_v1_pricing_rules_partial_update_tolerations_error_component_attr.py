from typing import Literal

ApiV1PricingRulesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_RULES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_rules_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingRulesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_RULES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
