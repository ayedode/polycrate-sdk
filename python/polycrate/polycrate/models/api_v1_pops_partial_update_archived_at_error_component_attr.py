from typing import Literal

ApiV1PopsPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_POPS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pops_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
