from typing import Literal

ApiV1PricingRulesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_RULES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingRulesUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_pricing_rules_update_name_error_component_attr(
    value: str,
) -> ApiV1PricingRulesUpdateNameErrorComponentAttr:
    if value in API_V1_PRICING_RULES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
