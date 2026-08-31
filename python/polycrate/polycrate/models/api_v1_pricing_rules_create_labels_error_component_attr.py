from typing import Literal

ApiV1PricingRulesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_RULES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingRulesCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_pricing_rules_create_labels_error_component_attr(
    value: str,
) -> ApiV1PricingRulesCreateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_RULES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
