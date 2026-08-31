from typing import Literal

ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_cost_statements_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
