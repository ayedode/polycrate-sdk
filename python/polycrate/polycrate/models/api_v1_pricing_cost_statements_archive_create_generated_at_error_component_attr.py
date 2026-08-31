from typing import Literal

ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponentAttr = Literal["generated_at"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_GENERATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponentAttr
] = {
    "generated_at",
}


def check_api_v1_pricing_cost_statements_archive_create_generated_at_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_GENERATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_GENERATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
