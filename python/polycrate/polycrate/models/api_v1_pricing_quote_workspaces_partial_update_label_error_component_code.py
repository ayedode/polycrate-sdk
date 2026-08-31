from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_LABEL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_quote_workspaces_partial_update_label_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_LABEL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_LABEL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
