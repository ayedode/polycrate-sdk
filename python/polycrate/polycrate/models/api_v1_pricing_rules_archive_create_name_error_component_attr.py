from typing import Literal

ApiV1PricingRulesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_rules_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1PricingRulesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
