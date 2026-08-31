from typing import Literal

ApiV1PoliciesPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_POLICIES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_policies_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1PoliciesPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
