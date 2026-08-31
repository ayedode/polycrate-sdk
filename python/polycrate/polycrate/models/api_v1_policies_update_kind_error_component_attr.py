from typing import Literal

ApiV1PoliciesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_POLICIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_policies_update_kind_error_component_attr(value: str) -> ApiV1PoliciesUpdateKindErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
