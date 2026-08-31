from typing import Literal

ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_EXTERNAL_INVOICE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_cost_statements_generate_create_external_invoice_id_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_EXTERNAL_INVOICE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_EXTERNAL_INVOICE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
