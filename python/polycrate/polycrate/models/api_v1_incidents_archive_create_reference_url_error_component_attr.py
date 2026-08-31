from typing import Literal

ApiV1IncidentsArchiveCreateReferenceUrlErrorComponentAttr = Literal["reference_url"]

API_V1_INCIDENTS_ARCHIVE_CREATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateReferenceUrlErrorComponentAttr
] = {
    "reference_url",
}


def check_api_v1_incidents_archive_create_reference_url_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateReferenceUrlErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
