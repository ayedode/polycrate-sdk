from typing import Literal

ApiV1IncidentsCreateReporterErrorComponentAttr = Literal["reporter"]

API_V1_INCIDENTS_CREATE_REPORTER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsCreateReporterErrorComponentAttr] = {
    "reporter",
}


def check_api_v1_incidents_create_reporter_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateReporterErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_REPORTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_REPORTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
