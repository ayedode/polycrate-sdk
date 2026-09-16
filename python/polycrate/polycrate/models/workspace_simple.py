from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workspace_kind_enum import WorkspaceKindEnum, check_workspace_kind_enum

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="WorkspaceSimple")


@_attrs_define
class WorkspaceSimple:
    """
    Attributes:
        id (UUID):
        name (str):
        display_name (None | str): The display name is used to display the object in the UI. It can be different from
            the name.
        reconciliation_running (bool):
        kind (WorkspaceKindEnum): * `polycrate` - Polycrate
            * `generic` - Generic
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        legacy (bool): Legacy workspaces have Git-Repos, non-legacy workspaces work only with Block-Infos from Polycrate
            API/UI
        url (str):
    """

    id: UUID
    name: str
    display_name: None | str
    reconciliation_running: bool
    kind: WorkspaceKindEnum
    organization: OrganizationSimple
    legacy: bool
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        display_name: None | str
        display_name = self.display_name

        reconciliation_running = self.reconciliation_running

        kind: str = self.kind

        organization = self.organization.to_dict()

        legacy = self.legacy

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "reconciliation_running": reconciliation_running,
                "kind": kind,
                "organization": organization,
                "legacy": legacy,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        reconciliation_running = d.pop("reconciliation_running")

        kind = check_workspace_kind_enum(d.pop("kind"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        legacy = d.pop("legacy")

        url = d.pop("url")

        workspace_simple = cls(
            id=id,
            name=name,
            display_name=display_name,
            reconciliation_running=reconciliation_running,
            kind=kind,
            organization=organization,
            legacy=legacy,
            url=url,
        )

        workspace_simple.additional_properties = d
        return workspace_simple

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
