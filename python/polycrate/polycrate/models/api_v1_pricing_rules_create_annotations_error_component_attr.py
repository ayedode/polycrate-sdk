from typing import Literal

ApiV1PricingRulesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_RULES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_rules_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingRulesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_RULES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
