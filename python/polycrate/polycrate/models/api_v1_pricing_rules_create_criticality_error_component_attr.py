from typing import Literal

ApiV1PricingRulesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_RULES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_rules_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingRulesCreateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_RULES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
