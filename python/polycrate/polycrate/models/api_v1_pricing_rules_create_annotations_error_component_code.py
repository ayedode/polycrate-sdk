from typing import Literal

ApiV1PricingRulesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_RULES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_rules_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingRulesCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_RULES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
