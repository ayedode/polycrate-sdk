from typing import Literal

IssuerKindEnum = Literal["clusterissuer", "issuer"]

ISSUER_KIND_ENUM_VALUES: set[IssuerKindEnum] = {
    "clusterissuer",
    "issuer",
}


def check_issuer_kind_enum(value: str) -> IssuerKindEnum:
    if value in ISSUER_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ISSUER_KIND_ENUM_VALUES!r}")
