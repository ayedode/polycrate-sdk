from typing import Literal

ApiV1CvesPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_CVES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_cves_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
