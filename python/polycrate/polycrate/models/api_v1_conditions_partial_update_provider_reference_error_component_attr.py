from typing import Literal

ApiV1ConditionsPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_CONDITIONS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_conditions_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1ConditionsPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
