from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceReportGenerateRequestRequest")


@_attrs_define
class ComplianceReportGenerateRequestRequest:
    """
    Attributes:
        organization (UUID):
        period_start (datetime.date | Unset):
        period_end (datetime.date | Unset):
        force (bool | Unset):  Default: False.
    """

    organization: UUID
    period_start: datetime.date | Unset = UNSET
    period_end: datetime.date | Unset = UNSET
    force: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization = str(self.organization)

        period_start: str | Unset = UNSET
        if not isinstance(self.period_start, Unset):
            period_start = self.period_start.isoformat()

        period_end: str | Unset = UNSET
        if not isinstance(self.period_end, Unset):
            period_end = self.period_end.isoformat()

        force = self.force

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization": organization,
            }
        )
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("organization", (None, str(self.organization), "text/plain")))

        if not isinstance(self.period_start, Unset):
            files.append(("period_start", (None, self.period_start.isoformat().encode(), "text/plain")))

        if not isinstance(self.period_end, Unset):
            files.append(("period_end", (None, self.period_end.isoformat().encode(), "text/plain")))

        if not isinstance(self.force, Unset):
            files.append(("force", (None, str(self.force).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization = UUID(d.pop("organization"))

        _period_start = d.pop("period_start", UNSET)
        period_start: datetime.date | Unset
        if isinstance(_period_start, Unset):
            period_start = UNSET
        else:
            period_start = datetime.date.fromisoformat(_period_start)

        _period_end = d.pop("period_end", UNSET)
        period_end: datetime.date | Unset
        if isinstance(_period_end, Unset):
            period_end = UNSET
        else:
            period_end = datetime.date.fromisoformat(_period_end)

        force = d.pop("force", UNSET)

        compliance_report_generate_request_request = cls(
            organization=organization,
            period_start=period_start,
            period_end=period_end,
            force=force,
        )

        compliance_report_generate_request_request.additional_properties = d
        return compliance_report_generate_request_request

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
