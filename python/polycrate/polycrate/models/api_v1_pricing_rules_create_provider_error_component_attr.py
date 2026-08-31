from typing import Literal

ApiV1PricingRulesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_RULES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_rules_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingRulesCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_RULES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
