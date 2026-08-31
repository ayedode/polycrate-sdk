from typing import Literal

ApiV1PoliciesUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_POLICIES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesUpdateArchivedAtErrorComponentAttr] = {
    "archived_at",
}


def check_api_v1_policies_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1PoliciesUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
