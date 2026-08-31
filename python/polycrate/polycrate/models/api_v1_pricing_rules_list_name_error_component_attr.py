from typing import Literal

ApiV1PricingRulesListNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_RULES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingRulesListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_pricing_rules_list_name_error_component_attr(
    value: str,
) -> ApiV1PricingRulesListNameErrorComponentAttr:
    if value in API_V1_PRICING_RULES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
