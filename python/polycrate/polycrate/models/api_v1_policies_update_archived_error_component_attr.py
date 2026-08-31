from typing import Literal

ApiV1PoliciesUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_POLICIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesUpdateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1_policies_update_archived_error_component_attr(
    value: str,
) -> ApiV1PoliciesUpdateArchivedErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
