from typing import Literal

ApiV1PoliciesPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_POLICIES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_policies_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1PoliciesPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
