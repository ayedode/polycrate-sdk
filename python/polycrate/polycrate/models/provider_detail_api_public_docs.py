from typing import Literal

ProviderDetailApiPublicDocs = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_API_PUBLIC_DOCS_VALUES: set[ProviderDetailApiPublicDocs] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_api_public_docs(value: str) -> ProviderDetailApiPublicDocs:
    if value in PROVIDER_DETAIL_API_PUBLIC_DOCS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_API_PUBLIC_DOCS_VALUES!r}")
