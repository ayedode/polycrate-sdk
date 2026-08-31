from typing import Literal

ApiV1PoliciesCreateModelsSelectorErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_CREATE_MODELS_SELECTOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesCreateModelsSelectorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_create_models_selector_error_component_code(
    value: str,
) -> ApiV1PoliciesCreateModelsSelectorErrorComponentCode:
    if value in API_V1_POLICIES_CREATE_MODELS_SELECTOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_MODELS_SELECTOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
