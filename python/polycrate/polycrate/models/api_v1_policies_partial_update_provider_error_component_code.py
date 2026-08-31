from typing import Literal

ApiV1PoliciesPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_POLICIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_policies_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1PoliciesPartialUpdateProviderErrorComponentCode:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
