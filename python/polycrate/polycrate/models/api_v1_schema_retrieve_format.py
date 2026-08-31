from typing import Literal

ApiV1SchemaRetrieveFormat = Literal["json", "yaml"]

API_V1_SCHEMA_RETRIEVE_FORMAT_VALUES: set[ApiV1SchemaRetrieveFormat] = {
    "json",
    "yaml",
}


def check_api_v1_schema_retrieve_format(value: str) -> ApiV1SchemaRetrieveFormat:
    if value in API_V1_SCHEMA_RETRIEVE_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_SCHEMA_RETRIEVE_FORMAT_VALUES!r}")
