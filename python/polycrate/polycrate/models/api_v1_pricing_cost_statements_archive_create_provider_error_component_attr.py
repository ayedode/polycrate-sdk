from typing import Literal

ApiV1PricingCostStatementsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_cost_statements_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
