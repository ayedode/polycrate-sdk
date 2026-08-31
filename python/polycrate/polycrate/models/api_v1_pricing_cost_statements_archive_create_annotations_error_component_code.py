from typing import Literal

ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_cost_statements_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
