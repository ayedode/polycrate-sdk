from typing import Literal

ApiV1PoliciesCreateKindsSelectorErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesCreateKindsSelectorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_create_kinds_selector_error_component_code(
    value: str,
) -> ApiV1PoliciesCreateKindsSelectorErrorComponentCode:
    if value in API_V1_POLICIES_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
