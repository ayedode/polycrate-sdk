from typing import Literal

ApiV1PricingRulesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_RULES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingRulesUpdateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_pricing_rules_update_labels_error_component_attr(
    value: str,
) -> ApiV1PricingRulesUpdateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_RULES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
