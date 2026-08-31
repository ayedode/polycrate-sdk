from typing import Literal

ApiV1PoliciesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_create_tolerations_error_component_code(
    value: str,
) -> ApiV1PoliciesCreateTolerationsErrorComponentCode:
    if value in API_V1_POLICIES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
