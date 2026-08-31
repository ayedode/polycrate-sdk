from typing import Literal

ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_cost_statements_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
