from typing import Literal

ApiV1PoliciesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_POLICIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_policies_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1PoliciesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
