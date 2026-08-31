from typing import Literal

ApiV1PoliciesUpdateModelsSelectorErrorComponentAttr = Literal["models_selector"]

API_V1_POLICIES_UPDATE_MODELS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesUpdateModelsSelectorErrorComponentAttr
] = {
    "models_selector",
}


def check_api_v1_policies_update_models_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesUpdateModelsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_MODELS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_MODELS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
