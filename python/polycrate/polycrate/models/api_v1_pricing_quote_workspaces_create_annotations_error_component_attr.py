from typing import Literal

ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_quote_workspaces_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
