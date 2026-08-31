from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DNSImportRecordsResponse")


@_attrs_define
class DNSImportRecordsResponse:
    """
    Attributes:
        created (int): Number of successfully created records.
        skipped (int): Number of skipped records (SOA, NSEC, etc.).
        errors (list[str]): Per-record error messages.
    """

    created: int
    skipped: int
    errors: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        skipped = self.skipped

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "skipped": skipped,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        skipped = d.pop("skipped")

        errors = cast(list[str], d.pop("errors"))

        dns_import_records_response = cls(
            created=created,
            skipped=skipped,
            errors=errors,
        )

        dns_import_records_response.additional_properties = d
        return dns_import_records_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
