from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_quote_workspaces_update_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
