from typing import Literal

ApiV1ConditionsPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_CONDITIONS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_conditions_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1ConditionsPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
