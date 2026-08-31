from typing import Literal

ApiV1CvesPartialUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_CVES_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesPartialUpdateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_cves_partial_update_scope_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdateScopeErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
