from typing import Literal

ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponentAttr = Literal["external_invoice_id"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_EXTERNAL_INVOICE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponentAttr
] = {
    "external_invoice_id",
}


def check_api_v1_pricing_cost_statements_partial_update_external_invoice_id_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_EXTERNAL_INVOICE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_EXTERNAL_INVOICE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
