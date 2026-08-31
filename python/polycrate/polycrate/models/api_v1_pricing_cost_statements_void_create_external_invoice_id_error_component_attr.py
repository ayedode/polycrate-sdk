from typing import Literal

ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponentAttr = Literal["external_invoice_id"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_EXTERNAL_INVOICE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponentAttr
] = {
    "external_invoice_id",
}


def check_api_v1_pricing_cost_statements_void_create_external_invoice_id_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_EXTERNAL_INVOICE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_EXTERNAL_INVOICE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
