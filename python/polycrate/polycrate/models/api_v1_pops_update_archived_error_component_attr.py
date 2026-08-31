from typing import Literal

ApiV1PopsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_POPS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsUpdateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1_pops_update_archived_error_component_attr(value: str) -> ApiV1PopsUpdateArchivedErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
