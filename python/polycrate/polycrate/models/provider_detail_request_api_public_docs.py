from typing import Literal

ProviderDetailRequestApiPublicDocs = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_REQUEST_API_PUBLIC_DOCS_VALUES: set[ProviderDetailRequestApiPublicDocs] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_request_api_public_docs(value: str) -> ProviderDetailRequestApiPublicDocs:
    if value in PROVIDER_DETAIL_REQUEST_API_PUBLIC_DOCS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_API_PUBLIC_DOCS_VALUES!r}")
