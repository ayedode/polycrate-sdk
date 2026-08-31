from typing import Literal

ApiV1PricingRulesArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingRulesArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_rules_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingRulesArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
