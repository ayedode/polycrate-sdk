from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_quote_workspaces_archive_create_display_name_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
