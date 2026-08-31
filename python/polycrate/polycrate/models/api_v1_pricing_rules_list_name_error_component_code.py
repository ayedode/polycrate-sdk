from typing import Literal

ApiV1PricingRulesListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_PRICING_RULES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PricingRulesListNameErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_pricing_rules_list_name_error_component_code(
    value: str,
) -> ApiV1PricingRulesListNameErrorComponentCode:
    if value in API_V1_PRICING_RULES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
