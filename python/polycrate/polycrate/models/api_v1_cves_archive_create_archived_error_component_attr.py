from typing import Literal

ApiV1CvesArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_CVES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_cves_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1CvesArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_CVES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
