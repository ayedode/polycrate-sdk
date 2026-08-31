from typing import Literal

ApiV1PricingRulesArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_rules_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1PricingRulesArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
