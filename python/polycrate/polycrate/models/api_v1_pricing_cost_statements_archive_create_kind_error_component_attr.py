from typing import Literal

ApiV1PricingCostStatementsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_cost_statements_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
