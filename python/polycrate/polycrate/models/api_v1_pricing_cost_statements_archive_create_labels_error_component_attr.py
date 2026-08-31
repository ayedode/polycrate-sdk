from typing import Literal

ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_cost_statements_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
