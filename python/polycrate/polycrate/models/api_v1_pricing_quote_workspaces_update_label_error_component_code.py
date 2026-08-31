from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LABEL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_quote_workspaces_update_label_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LABEL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LABEL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
