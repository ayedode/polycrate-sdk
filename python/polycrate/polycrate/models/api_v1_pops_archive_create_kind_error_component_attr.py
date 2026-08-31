from typing import Literal

ApiV1PopsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_POPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsArchiveCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_pops_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1PopsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_POPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
