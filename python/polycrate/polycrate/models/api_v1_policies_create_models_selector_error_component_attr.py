from typing import Literal

ApiV1PoliciesCreateModelsSelectorErrorComponentAttr = Literal["models_selector"]

API_V1_POLICIES_CREATE_MODELS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesCreateModelsSelectorErrorComponentAttr
] = {
    "models_selector",
}


def check_api_v1_policies_create_models_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesCreateModelsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_CREATE_MODELS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_MODELS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
