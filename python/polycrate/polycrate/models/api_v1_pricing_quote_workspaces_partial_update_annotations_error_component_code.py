from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_quote_workspaces_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
