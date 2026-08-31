from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.severity_401_enum import Severity401Enum, check_severity_401_enum
from ..models.status_a85_enum import StatusA85Enum, check_status_a85_enum

T = TypeVar("T", bound="CVESimple")


@_attrs_define
class CVESimple:
    """Simple serializer for embedding CVE in other serializers (e.g. VulnerabilityFinding).

    Attributes:
        id (UUID):
        name (str):
        display_name (None | str): The display name is used to display the object in the UI. It can be different from
            the name.
        cve_id (str): Canonical CVE identifier, e.g. CVE-2024-12345
        title (str): Short human-readable title/summary
        severity (Severity401Enum): * `critical` - Critical
            * `high` - High
            * `medium` - Medium
            * `low` - Low
            * `none` - None
            * `unknown` - Unknown
        status (StatusA85Enum): * `open` - Open
            * `disputed` - Disputed
            * `rejected` - Rejected
            * `reserved` - Reserved
        cvss_score (None | str): CVSS base score (0.0 - 10.0)
        url (str):
    """

    id: UUID
    name: str
    display_name: None | str
    cve_id: str
    title: str
    severity: Severity401Enum
    status: StatusA85Enum
    cvss_score: None | str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        display_name: None | str
        display_name = self.display_name

        cve_id = self.cve_id

        title = self.title

        severity: str = self.severity

        status: str = self.status

        cvss_score: None | str
        cvss_score = self.cvss_score

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "cve_id": cve_id,
                "title": title,
                "severity": severity,
                "status": status,
                "cvss_score": cvss_score,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        cve_id = d.pop("cve_id")

        title = d.pop("title")

        severity = check_severity_401_enum(d.pop("severity"))

        status = check_status_a85_enum(d.pop("status"))

        def _parse_cvss_score(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cvss_score = _parse_cvss_score(d.pop("cvss_score"))

        url = d.pop("url")

        cve_simple = cls(
            id=id,
            name=name,
            display_name=display_name,
            cve_id=cve_id,
            title=title,
            severity=severity,
            status=status,
            cvss_score=cvss_score,
            url=url,
        )

        cve_simple.additional_properties = d
        return cve_simple

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
