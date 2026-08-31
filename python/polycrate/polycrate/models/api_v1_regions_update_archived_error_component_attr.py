from typing import Literal

ApiV1RegionsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_REGIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsUpdateArchivedErrorComponentAttr] = {
    "archived",
}


def check_api_v1_regions_update_archived_error_component_attr(
    value: str,
) -> ApiV1RegionsUpdateArchivedErrorComponentAttr:
    if value in API_V1_REGIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
