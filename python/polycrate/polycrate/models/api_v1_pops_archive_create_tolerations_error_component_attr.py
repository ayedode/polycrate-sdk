from typing import Literal

ApiV1PopsArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_POPS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pops_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PopsArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_POPS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
