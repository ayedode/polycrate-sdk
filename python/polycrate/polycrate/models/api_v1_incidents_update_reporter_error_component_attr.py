from typing import Literal

ApiV1IncidentsUpdateReporterErrorComponentAttr = Literal["reporter"]

API_V1_INCIDENTS_UPDATE_REPORTER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsUpdateReporterErrorComponentAttr] = {
    "reporter",
}


def check_api_v1_incidents_update_reporter_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateReporterErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_REPORTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_REPORTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
