from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_QUOTE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_pricing_quote_workspaces_archive_create_quote_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_QUOTE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_QUOTE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
