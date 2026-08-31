from typing import Literal

ApiV1PricingRulesPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PRICING_RULES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_pricing_rules_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1PricingRulesPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_PRICING_RULES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
