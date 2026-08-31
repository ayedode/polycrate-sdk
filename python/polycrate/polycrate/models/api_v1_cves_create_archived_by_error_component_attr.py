from typing import Literal

ApiV1CvesCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_CVES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateArchivedByErrorComponentAttr] = {
    "archived_by",
}


def check_api_v1_cves_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1CvesCreateArchivedByErrorComponentAttr:
    if value in API_V1_CVES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
