from typing import Literal

ApiV1CvesUpdateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_CVES_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateArchivedByErrorComponentAttr] = {
    "archived_by",
}


def check_api_v1_cves_update_archived_by_error_component_attr(
    value: str,
) -> ApiV1CvesUpdateArchivedByErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
